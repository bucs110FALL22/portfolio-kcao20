replacement = {
    "executive": "big boss",
    "employees": "minions",
    "Kraken": "scary sea monster",
    "tech": "magic",
    "technology": "study of magic",
    "company": "cool place"
}

text = """

Technology|C.E.O. of Kraken, the Cryptocurrency Exchange, Steps Down

Jesse Powell, the chief executive, has battled with employees after posting messages about race and gender and urging those who disagreed with his values to leave.

Sept. 21, 2022, 3:58 p.m. ET

Jesse Powell, a founder of the cryptocurrency exchange Kraken, is stepping down as chief executive.

Mr. Powell will be replaced by Dave Ripley, the chief operating officer, Kraken said on Wednesday. The transition is set to take place in the next few months after the company finds a replacement for Mr. Ripley. Mr. Powell will remain at Kraken as chairman.

An early Bitcoin entrepreneur, Mr. Powell has been embroiled in conflict with Kraken employees after he posted inflammatory messages this year about race and gender on the company’s Slack. He urged those who disagreed with his values to leave the company. Some did.

Kraken also faces an investigation by the Treasury Department over potential violations of U.S. sanctions. The department is expected to fine Kraken, The New York Times reported in July.

In a blog post, Kraken said that Mr. Ripley, who joined the company after it acquired his start-up in 2016, was chosen following a “rigorous internal and external search” over the past year. Mr. Powell planned to spend more of his time focusing on “the company’s products, user experience and broader industry advocacy,” the company said.

Mr. Powell and Thanh Luu founded Kraken in 2011 as one of the first major exchanges for investors to buy and sell digital assets. Kraken was eventually overtaken by Coinbase and now ranks as the second-largest exchange in the United States, according to CoinMarketCap, an industry data tracker. Last year, Mr. Powell said he was considering taking the company public.

The conflict at Kraken began this spring after Mr. Powell questioned employees’ use of preferred pronouns and engaged in a lengthy discussion about whether women are inherently less intelligent than men.

Some employees voiced complaints, and Mr. Powell released a company culture document outlining what he described as Kraken’s libertarian values. He told employees that if they disagreed with the document, they should quit. In response to reporting by The Times on Kraken’s internal conflict, he tweeted in June that he was returning the company “back to dictatorship.”

David Yaffe-Bellany covers cryptocurrencies and fintech. He graduated from Yale University and previously reported in Texas, Ohio, Connecticut and Washington, D.C. @yaffebellany

Ryan Mac is a technology reporter focused on corporate accountability across the global tech industry. He won a 2020 George Polk award for his coverage of Facebook and is based in Los Angeles. @RMac18
"""

for word in replacement.keys():
    text = text.replace(word, replacement[word])

print(text)