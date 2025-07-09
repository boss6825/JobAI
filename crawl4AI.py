import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    browser_config = BrowserConfig(verbose=True)
    run_config = CrawlerRunConfig(
        # Content filtering
        word_count_threshold=10,
        excluded_tags=['form', 'header'],
        exclude_external_links=True,

        # Content processing
        process_iframes=True,
        remove_overlay_elements=True,

        # Cache control
        cache_mode=CacheMode.ENABLED  # Use cache if available
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.google.com/search?q=devops+jobs+in+noida+for+freshers&rlz=1C1RXQR_enIN1163IN1163&oq=devops+jobs+in+noida+for+freshers&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MggIARAAGBYYHjINCAIQABiGAxiABBiKBTINCAMQABiGAxiABBiKBTINCAQQABiGAxiABBiKBTINCAUQABiGAxiABBiKBTIKCAYQABiABBiiBDIHCAcQABjvBdIBCDQ3MzRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&jbr=sep:0#vhid=vt%3D20/docid%3D4vBePYjI5rcFYadQAAAAAA%3D%3D&vssid=jobs-detail-viewer",
            config=run_config
        )

        if result.success:
            # Print clean content
            print("Content:", result.markdown[:500])  # First 500 chars

            # Process images
            for image in result.media["images"]:
                print(f"Found image: {image['src']}")

            # Process links
            for link in result.links["internal"]:
                print(f"Internal link: {link['href']}")

        else:
            print(f"Crawl failed: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
