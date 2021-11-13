# Data scientist in Simple Stock Analysis of PT Bukalapak.com Tbk for Long Term Investment

## Brief explanation of PT Bukalapak.com Tbk
Bukalapak was founded on January 10, 2010 by Achmad Zaky, Nugroho Herucahyono, and Fajrin Rasyid in a boarding house while studying at the Bandung Institute of Technology.
Bukalapak is one of the e-commerce companies in Indonesia. From the owner of a local shopping brand through an ownership group founded by Achmad Zaky, Nugroho Herucahyono, and Muhamad Fajrin Rasyid in 2010. Bukalapak was originally an online store that allowed Small and Medium Enterprises (SMEs) to venture into cyberspace. The company has now expanded into various other business lines, including helping to increase sales of traditional warungs through the Bukalapak Partner service. In 2017, Bukalapak became one of the unicorn startups from Indonesia. Currently, Bukalapak's valuation has reached 7.6 billion US dollars or around Rp. 110.2 trillion.
## Bukalapak conducts Initial Public Offering of Shares
Bukalapak is the largest Initial Public Offering (IPO) company in Indonesia. This is the latest achievement that the Southeast Asian startup community is starting to grow.
Quoting **[CNN.com](https://www.cnnindonesia.com/ekonomi/20210807172937-92-677724/ipo-bukalapak-terbesar-sepanjang-sejarah)**, Saturday (8/7), Bukalapak reaped fresh funds of US $ 1.5 billion or Rp. 21.4 trillion (exchange rate of Rp. 14,300 per US dollar) from the corporate action.
When Bukalapak's shares were traded on the first day, the price immediately jumped almost 25% in the first session. This indicates that many investors are hunting for Bukalapak's shares.

Mandiri Sekuritas said Bukalapak's IPO was **oversubscribed by 8.7 times** with orders from nearly 100 thousand investors.
Bukalapak itself has developed into an e-commerce player in Southeast Asia. Some of Bukalapak's competitors, including Shopee, Lazada, and Tokopedia.

The company is backed by major investors, including **Microsoft (MSFT)** and **Standard Chartered (SCBFF)**.
The company plans to use the funds from the IPO to roll out more features. This will allow Bukalapak to offer more services and add new revenue streams.
Indonesia's first unicorn to be listed on the stock exchange has great potential. BUKA is part of a conglomerate that has penetrated into various potential business lines.

As a data analyst, we can do a simple analysis on Bukalapak shares to assess whether the benefits provided are tempting for investors? or is it detrimental? on a long term basis.
Through this simple analysis, we will calculate the **Return On Investment** on the Bukalapak stock

## Simple Stock Analysis for Long Term Investment

### A. Questions and Goals
- If we want to invest in long-term intervals, how can we reduce risk while maximizing return on investment?
- What is the best way to select stocks based on the criteria from the previous question?
The purpose of this analysis is to look at Bukalapak's stock in providing a return on investment considering the risks involved. The analysis must provide substantial data to confidently use the stock for future analysis or use.

### B. Data Collection
There are many ways to aggregate historical stock prices with their fundamentals. For this particular analysis, [Pandas](https://pandas.pydata.org/) provides a library for retrieving forum data from multiple sources. The library is called `Pandas Data Reader`. The library is a wrapper for retrieving data like historical stock prices, country GDP, World economic data, etc. This analysis in particular. [Yahoo Finance](https://finance.yahoo.com/quote/BUKA.JK?p=BUKA.JK&.tsrc=fin-srch) data is used because it is free and has a very large stock database. By avoiding manual, tedious work like downloading CSV files, analysis can be used for as much stock as possible. By doing `import pandas_datareader.data as web`

Since the final analysis will involve a return on investment, the Closing price is Adjusted. Used This option was taken to simplify the analysis. also, based on the adjusted closing price period, the price should best reflect the BUKA price on a given day.
#### Plotting Price BUKA Stock
![download (3)](https://user-images.githubusercontent.com/91531966/141608697-84a9b465-ba67-4a7b-a0f0-55e3722766b4.png)

The plot above shows the price of **BUKA** from the beginning of the IPO until November 2021. As expected, the data has shown a clear trend, namely a down trend. For example, let's take the return on investment if someone returns the money at the start of the IPO. Since plots of the same style will be widely used in this analysis, functions can be written to simplify future use.
