# CaptureWechatArticle
Capture Wechat Article with Selenium

Selenium真的是太棒辣！
本项目用作北京大学南燕就业发布的实习、校招文章图片截图。需要提前写个小爬虫获取公众号文章链接，本项目有公众号账号，XPATH一下就出来了hiahiahia~

不过仍然存在一些问题待解决：由于网络问题，以图片为主的公众号文章会出现某部分图片没有加载出来导致截图出现空白的情况，利用visibility判断图片是否加载完成好像也没有解决此问题。
其他的解决办法大部分都是多等一会，有时间的时候可以再熟悉一下selenium以及EC.visibility_of_element_located的用法
