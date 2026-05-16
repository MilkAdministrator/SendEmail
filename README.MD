# SEND EMAIL
一个可以发送邮件的PYTHON脚本
# 使用方法
在"main.py"文件同目录下添加".content"与".json"文件,".content"为邮件内容文件,".json"为邮件配置文件,这是一个邮件配置文件的示例:
{
    "smtpserver":"smtp.example.com",
    "smtpport":000,
    "fromemail":"from@example.com",
    "toemail":"to@example.com",
    "password":"password",
    "subject":"subject",
    "type":"plain"
}
smtpserver为SMTP服务器,smtpport为SMTP端口,fromemail为发件人邮箱,toemail为收件人邮箱,password为邮箱密码,subject为邮件主题,type为邮件类型
