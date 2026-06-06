from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from bs4 import BeautifulSoup
import pandas as pd
import asyncio

async def save_login_session():
    async with Stealth().use_async(async_playwright()) as p:
        
        browser = await p.chromium.launch(
            headless=False,
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )
        
        USER_AGENT = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )

        context = await browser.new_context(
            user_agent=USER_AGENT
        )
        
        page = await context.new_page()
        
        print("Opening IMDb login page in Stealth Mode...")
        await page.goto("https://www.imdb.com/registration/signin")
        
        print("⏳ You have 60 seconds to log in manually using Google...")
        try:
            print("⏳ Login manually and press ENTER here when done...")
            input()
        except:
            pass
        
        print("Saving your session cookies...")
        await context.storage_state(path="imdb_session.json")
        
        await browser.close()
        print("✅ Session saved successfully to 'imdb_session.json'!")

# Run the generator
asyncio.run(save_login_session())

url = "https://www.imdb.com/title/tt1187043/reviews/"

async def scroll_and_fetch_html():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )
        
        USER_AGENT = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )

        context = await browser.new_context(
            user_agent=USER_AGENT, 
            storage_state="imdb_session.json"
        )
        
        page = await context.new_page()
        
        print("Loading page as an authenticated user...")
        await page.goto(url)
        
        # THE FIX: Explicitly wait for the body to exist and let React settle
        print("Waiting for the page to physically render...")
        await page.wait_for_selector("body", timeout=15000)
        await page.wait_for_timeout(3000)
        
        print("Starting dynamic scroll to load ALL reviews...")
        
        previous_count = 0
        retries = 0
        
        while True:
            # THE FIX: A safer javascript scroll that won't crash if the body temporarily vanishes
            await page.evaluate("if (document.body) window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000) 
            
            try:
                load_more_button = page.locator('button.ipc-see-more__button, button:has-text("more"), button:has-text("See all")').first
                if await load_more_button.is_visible(timeout=1000):
                    await load_more_button.click()
                    await page.wait_for_timeout(2000)
            except Exception:
                pass 
                
            current_cards = page.locator('.ipc-list-card, .review-container, article')
            current_count = await current_cards.count()
            
            if current_count == previous_count:
                retries += 1
                if retries >= 3:
                    print("Reached the absolute bottom of the page!")
                    break
            else:
                print(f"Loaded {current_count} reviews on screen so far...")
                retries = 0 
                previous_count = current_count
        
        print("Grabbing raw HTML for lightning-fast parsing...")
        html_content = await page.content()
        await page.close()

        await browser.close()
        return html_content

# 1. Use Playwright to load the page
raw_html = asyncio.run(scroll_and_fetch_html())

# 2. Use BeautifulSoup to extract the data instantly in memory
print("Parsing data with BeautifulSoup...")
soup = BeautifulSoup(raw_html, 'html.parser')

data = []

# Find all review containers
all_cards = soup.find_all('article')

print(f"Found {len(all_cards)} review cards")

for idx, card in enumerate(all_cards):

    # Username
    user_span = card.find('span', class_=lambda c: c and 'ipc-title__subtext' in c)
    username = user_span.text.strip() if user_span else "Unknown"

    # Rating
    rating_span = card.find('span', class_='ipc-rating-star--rating')
    rating = rating_span.text.strip() if rating_span else "5"

    # Review text
    text_div = card.find('div', class_='ipc-html-content-inner-div')
    review_text = text_div.text.strip() if text_div else "No Review"

    # Review Type
    try:
        rating_num = float(rating)

        if rating_num >= 7:
            review_type = "Positive"
        elif rating_num >= 5:
            review_type = "Neutral"
        else:
            review_type = "Negative"

    except:
        review_type = "Neutral"

    data.append({
        'Reviewer_No': idx + 1,
        'Rating': rating,
        'Review_Type': review_type,
        'Review_Comment': review_text,
        'Source': 'IMDb'
    })

# Create DataFrame
df = pd.DataFrame(data)

print(f"🎉 Success! Created DataFrame with {len(df)} reviews.")

# Save CSV
df.to_csv('3idiots_reviews.csv', index=False, encoding='utf-8')

print("CSV file saved successfully!")