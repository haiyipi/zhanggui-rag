多协议嵌入式以太网打印服务器和无线 (IEEE 802.11b/g) 以太网打印服务器

# 网络使用说明书

# HL-3040CN HL-3070CW

请在使用设备之前，仔细阅读使用说明书。将随机光盘放置在方便的地方，以便随时迅速查询。

请访问 http://solutions.brother.com/，您可以获取更多产品支持信息、最新的驱动程序升级和实用程序以及常见问题解答 (FAQ)和技术问题等。

# 本说明书使用的符号

本使用说明书使用以下图标：

<table><tr><td>重要事项</td><td>重要事项图标表示可能导致财产损失或产品功能丧失的潜在危险情况。</td></tr><tr><td><img src="images/58742e8c8fad04812cc998fa5084a32186978130d8887dca8f6eab592c976f21.jpg"/> 注释</td><td>此图标提醒您如何应对可能出现的情况或提供有关当前操作如何与其他功能工作的提示。</td></tr></table>

# 商标

brother 标识是兄弟工业株式会社的注册商标。

brother 是兄弟工业株式会社的注册商标。

Microsoft、Windows、Windows Server、Outlook 和 Internet Explorer 是微软公司在美国或其他国家的注册商标。

Windows Vista 是微软公司在美国和其他国家的注册商标或商标。

Apple、 Macintosh、 Safari 和 TrueType 是苹果公司在美国和其他国家的注册商标。

Linux 是 Linus Torvalds 在美国和其他国家的注册商标。

UNIX 是 Open 集团在美国和其他国家的注册商标。

Adobe、Flash、Illustrator、Photoshop、PostScript 和 PostScript 3 是 Adobe Systems Incorporated 在美国或其他国家的注册商标或商标。

BROADCOM、SecureEasySetup 和 SecureEasySetup 标识是 Broadcom 公司在美国和 / 或其他国家的商标或注册商标。

WPA、WPA2、Wi-Fi Protected Access 和 Wi-Fi Protected Setup 是 Wi-Fi Alliance 在美国或其他国家的商标或注册商标。

Wi-Fi 和 Wi-Fi Alliance 是 Wi-Fi Alliance 的注册商标。

AOSS 是 Buffalo 公司的商标。

Brother 产品、相关文档和任何其他资料中涉及的所有其他术语、品牌和产品名称都是其相应公司的商标或注册商标。

# 编辑及出版说明

本手册在兄弟工业株式会社监督下编辑出版，包含最新的产品说明与产品规格。

本手册内容及产品规格如有更改，恕不另行通知。

Brother 公司保留对包含在本手册中的产品规格和材料作出更改的权利，恕不另行通知，同时由于使用本手册包含的内容所造成的任何损坏 (包括后果 )，包括但不限于本出版物的排版及其他错误， Brother 公司将不承担任何责任。

©2009 Brother Industries Ltd.

# 重要注释

 本产品仅允许在购买国使用。  
请勿在购买国以外的国家使用本产品，因其可能违反该国关于无线通讯和电源的规定。  
 Windows® XP 在本说明书中是指 Windows® XP 专业版、Windows® XP 专业版 x64 版本和 Windows® XP家庭版。  
 Windows Server® 2003 在本说明书中是指 Windows Server® 2003 和 Windows Server® 2003 x64 版本。  
 Windows Server® 2008 在本说明书中是指 Windows Server® 2008 和 Windows Server® 2008 R2。  
 Windows Vista® 在本说明书中是指 Windows Vista® 的所有版本。  
 本说明书中的 Windows® 7 是指 Windows® 7 的所有版本。  
 打印机插图基于 HL-3070CW。

# Brother 联系方式

# 重要事项

如需获取技术支持和操作帮助，您必须拨打设备购买国的服务电话，且必须在购买国内拨打。

# 服务中心地址

请联系当地的 Brother 办事处，以查询中国境内的服务中心。可登录以下网站查询中国办事处的地址与联系电话等信息：http://www.brother-cn.net/。

# 网址

Brother 全球网址：http://www.brother.com/。

关于常见问题解答 (FAQ)、产品支持、驱动程序升级与实用程序，请登录以下网站查询：http://solutions.brother.com/。

# 目录

# 1 简介 1

概述 .

网络功能特性中 . ..2

网络打印中 . .2

管理实用程序中.. .2

网络连接的类型中 .4

网络连接示例中 . 4

无线网络连接示例 ( 适用于 HL-3070CW)中 . .6

协议中 .. ..7

TCP/IP 协议和功能中 .

其他协议中 . .9

# 2 配置网络设备 10

概述中 .. ..10

IP 地址、子网掩码和网关中. ..10

IP 地址中 . ..10

子网掩码中 . ..11

网关 ( 和路由器 )中 . ..11

步骤流程图中 ..12

设置 IP 地址和子网掩码. ..13

使用 BRAdmin Light 实用程序配置网络打印机中 ..13

使用操作面板配置网络设备. ..15

使用其他方式配置网络设备. ..15

更改打印服务器设置中. ..16

使用 BRAdmin Light 实用程序更改打印服务器设置中 ..16

使用 BRAdmin 专业版 3 实用程序更改打印服务器设置 ( 适用于 Windows®)中 .16

使用网络基本管理 ( 网络浏览器 ) 更改打印服务器设置. .17

使用操作面板更改打印服务器设置中 ..17

使用其他方式更改打印服务器设置中 ..17

# 3 配置无线网络设备 ( 适用于 HL-3070CW) 18

概述中 .. ..18

无线网络术语和概念中 ............. ..19

SSID ( 服务区标识符 ) 和信道中 . .19

验证和加密中 . ...19

无线网络配置步骤流程图中. .22

基础架构模式中 .. ..22

确认您的网络环境中. ..23

通过网络中的接入点连接至计算机 ( 基础架构模式 ) . .23

确认无线网络设置方式中 . ..24

使用随机光盘上的 Brother 安装程序配置无线网络设备 ( 推荐 )中.. .24

使用操作面板菜单中的 SES/WPS 或 AOSS 配置无线网络设备 (仅适用于基础架构模式 ).. .25

使用 Wi-Fi Protected Setup 的 PIN 方式配置无线网络设备 ( 仅适用于基础架构模式 )中.. .26

配置无线网络设备中.. ..27

使用随机光盘上的 Brother 安装程序配置无线网络设备 ( 推荐 )中.. .27

使用操作面板菜单中的 SES/WPS 或 AOSS 配置无线网络设备 .27

使用 Wi-Fi Protected Setup 的 PIN 方式配置无线网络设备中 .27

# 4 使用 Brother 自动安装程序进行的 Windows® 系统下的无线配置 ( 适用于 HL-3070CW) 28

在基础架构模式下进行的配置中. ..28

配置无线设置之前中 ..28

配置无线设置中. ..29

# 5 使用 Brother 安装程序进行的 Macintosh 系统下的无线配置 ( 适用于 HL-3070CW) 30

在基础架构模式下进行的配置中. ..30

配置无线设置之前中 ..30

配置无线设置中 . ..31

# 6 使用操作面板上的 SES/WPS 或 AOSS 进行的无线配置 ( 适用于 HL-3070CW) 39

概述中 .. ..39

如何使用操作面板菜单中的 SES/WPS 或 AOSS 配置无线设备中. .40

# 7 使用 Wi-Fi Protected Setup 的 PIN 方式的无线配置 ( 适用于 HL-3070CW) 43

概述中 . ..43

如何使用 Wi-Fi Protected Setup 的 PIN 方式配置无线设备中 ..43

Windows® 用户 :中 . .45

Macintosh 用户： ..49

# 8 操作面板功能 52

概述中 .52

网络菜单中 . ..53

TCP/IP中.. ..53

以太网 ( 仅适用于有线网络 )中 . ..61

恢复出厂设置中. ..61

设为默认值 ( 适用于 HL-3070CW)中 . ..61

启用有线网络 ( 仅适用于 HL-3070CW 有线网络 )中 ... ..62

启用无线网络 ( 仅适用于 HL-3070CW 无线网络 )中 .... ..62

SES/WPS 或 AOSS ( 仅适用于 HL-3070CW 无线网络 )中 .. ..62

有 PIN 密码的 WPS ( 仅适用于 HL-3070CW 无线网络 )中 ... ..63

无线网络状态 ( 仅适用于 HL-3070CW 无线网络 ) ... ..63

将网络设置恢复为出厂默认设置中. ..67

打印网络配置页中. ..68

# 9 驱动程序配置向导 ( 仅适用于 Windows®) 69

概述中 . ..69

连接方式中 .. ..69

对等中 ... ..69

网络共享中 .. ..70

本地打印机 (USB 接口电缆 )中 .. ..70

如何安装驱动程序配置向导软件 .71

使用驱动程序配置向导软件中. ..72

# 10 网络基本管理 75

概述中 .. ..75

如何使用网络基本管理 ( 网络浏览器) 配置打印服务器设置 ..76

# 11 在 Windows® 操作系统下进行网络打印：基本 TCP/IP 对等打印 77

概述中 . ..77

配置标准 TCP/IP 端口中 . ..78

尚未安装打印机驱动程序. ..78

已安装打印机驱动程序中 ..80

其他信息来源中 . ..80

# 12 在 Windows® 操作系统下进行网络打印 81

概述中 .. ..81

在 Windows® 操作系统下进行的 IPP 打印 .81

Windows Vista® 、 Windows® 7 和 Windows Server® 2008中 ..81

Windows® 2000/XP 和 Windows Server® 2003中 . ..83

指定一个不同的 URL中 . ..85

其他信息来源中 . ..85

# 13 在 Macintosh 操作系统下使用 BR-Script 3 驱动程序进行网络打印 ( 适用于 HL-3070CW) 86

概述中 .. ..86

如何选择打印机驱动程序 (TCP/IP)中 .. ..86

# 14 安全性能 90

概述中 .. ..90

安全术语中 . ..90

安全协议中 .. ..91

电子邮件通知的安全方法中. ..91

配置协议设置中 . ..92

安全管理网络打印机中. ..93

使用网络基本管理 ( 网络浏览器 ) 的安全管理中 ..93

使用 BRAdmin 专业版 3 的安全管理 ( 适用于 Windows®)中 ..96

安全功能锁 2.0 ( 适用于 HL-3070CW)中 ..97

如何使用网络基本管理 ( 网络浏览器 ) 配置安全功能锁 2.0. ..97

使用 IPPS 安全打印文档中 ..100

指定一个不同的 URL中 . ..100

使用带用户验证的电子邮件通知 ..101

创建并安装证书中 ..103

创建和安装自我认定证书中. ..105

创建 CSR 并安装证书中 ..118

导入和导出证书和机密键中 . .120

# 15 故障排除 121

概述中 .. ..121

常见问题中 . ..121

网络打印软件安装问题中 ..123

打印问题中 . ..125

与协议相关问题的故障排除方法 ..126

Windows® 2000/XP、Windows Vista® 、Windows® 7 和 Windows Server® 2003/2008IPP 故障排除中 . .126

网络基本管理 ( 网络浏览器 ) 故障排除 (TCP/IP)中 . .126

无线网络故障排除 ( 适用于 HL-3070CW)中. .127

无线连接问题中 . .127

# A 附录 128

使用服务. ..128

设置 IP 地址的其他方法 ( 适用于高级用户和管理员 )中 .. ..128

使用 DHCP 配置 IP 地址中. .128

使用 BOOTP 配置 IP 地址中.. .129

使用 RARP 配置 IP 地址中 . ..130

使用 APIPA 配置 IP 地址.. ..130

使用 ARP 配置 IP 地址 . ..131

使用 TELNET 控制台配置 IP 地址中. .132

使用 Brother Web BRAdmin 服务器软件对 IIS 进行 IP 地址的配置中 .133

使用网络打印队列或共享时的安装中 ..134

使用网络服务时的安装 ( 适用于 Windows Vista® 和 Windows® 7 用户 )中 .. ..135

# B 附录 136

打印服务器规格中 .. ..136

有线以太网中. .136

无线网络 ( 适用于 HL-3070CW)中 .. .137

功能表和出厂默认设置中 . ..138

# C 索引 141

# 1 简介

# 概述

通过使用内部网络打印服务器，可以在 10/100MB 有线或 IEEE 802.11b/802.11g 无线以太网上共享 Brother设备。打印服务器提供适用于支持 TCP/IP 协议的 Windows® 2000/XP、 Windows Vista®、 Windows® 7、Windows Server® 2003/2008 以及支持 TCP/IP 的 Macintosh (Mac OS X 10.3.9 或更高版本 )。下列表格显示各操作系统所支持的网络功能特性和连接。

<table><tr><td>操作系统</td><td>Windows® 2000/XPWindows Vista®Windows Server® 2003/2008Windows® 7</td><td>Mac OS X 10.3.9 或更高版本</td></tr><tr><td>10/100BASE-TX 有线以太网 (TCP/IP)</td><td>√</td><td>√</td></tr><tr><td>IEEE 802.11b/g 无线以太网 (TCP/IP) $^1$ </td><td>√</td><td>√</td></tr><tr><td>打印</td><td>√</td><td>√</td></tr><tr><td>BRAdmin Light</td><td>√</td><td>√</td></tr><tr><td>BRAdmin 专业版  $3^2$ </td><td>√</td><td></td></tr><tr><td>Web BRAdmin $^2$ </td><td>√</td><td></td></tr><tr><td>BRPrint Auditor $^{23}$ </td><td>√</td><td></td></tr><tr><td>网络基本管理 (网络浏览器)</td><td>√</td><td>√</td></tr><tr><td>因特网打印 (IPP)</td><td>√</td><td></td></tr><tr><td>状态监视器 $^4$ </td><td>√</td><td>√</td></tr><tr><td>驱动程序配置向导</td><td>√</td><td></td></tr></table>

1 仅 HL-3070CW 支持 IEEE 802.11b/g 无线以太网 (TCP/IP)。  
2 可登录 http://solutions.brother.com/ 网站下载 BRAdmin Professional 3、 Web BRAdmin 和 BRPrint Auditor。  
3 在通过 USB 接口连接到客户端计算机的设备上使用 BRAdmin 专业版 3 或 Web BRAdmin 时可用。  
4 如需获取更多信息，请参考随机光盘上的使用说明书。

若要通过网络使用 Brother 设备，您需要配置打印服务器，并设置您需要使用的计算机。

# 网络功能特性

Brother 设备拥有以下基本网络功能。

# 网络打印

打印服务器提供适用于支持 TCP/IP 协议的 Windows® 2000/XP、 Windows Vista® 、 Windows® 7 和Windows Server® 2003/2008 以及支持 TCP/IP 的 Macintosh (Mac OS X 10.3.9 或更高版本 ) 的打印服务。

# 管理实用程序

# BRAdmin Light

BRAdmin Light 是一个用于为连接网络的 Brother 设备进行初始设置的实用程序。该实用程序可以在您的网络中搜索 Brother 产品，查看状态并配置如 IP 地址等基本网络设置。 BRAdmin Light 实用程序可在Windows® 2000/XP、Windows Vista®、Windows® 7 和 Windows Server® 2003/2008 和 Mac OS X 10.3.9( 或更高版本 ) 的计算机上使用。关于在 Windows® 中安装 BRAdmin Light 的详细信息，请参考随机附带的快速安装指南。对于Macintosh 用户，当您安装打印机驱动程序时，BRAdmin Light软件将自动安装。如果已安装了打印机驱动程序，则不需要重新安装。

关于 BRAdmin Light 的详细信息，请访问以下网站：http://solutions.brother.com/。

# BRAdmin 专业版 3 ( 适用于 Windows®)

BRAdmin 专业版 3 是一个用于为连接网络的 Brother 设备进行更高级管理的实用程序。该实用程序可以在您的网络中搜索 Brother 产品，并可以通过一个简明的浏览器窗口查看设备状态，该窗口通过不同的颜色来反映各设备的不同状态。您可以配置网络和设备设置，同时还可以通过局域网中的 Windows® 计算机升级设备固件。BRAdmin 专业版 3 也可以记录所在网络中的 Brother 设备的活动，并以 HTML、CSV、TXT 或 SQL格式导出记录数据。

如果您想监控本地连接的打印机，请在客户端计算机上安装 BRPrint Auditor 软件。通过该实用程序，您可以使用 BRAdmin 专业版 3 监控通过 USB 接口电缆连接到客户端计算机的打印机。

如需获取更多信息或下载相关资料，请访问以下网站：http://solutions.brother.com/。

# Web BRAdmin ( 适用于 Windows®)

Web BRAdmin 是一个用于管理局域网和无线网络中的 Brother 设备的实用程序。该实用程序可以在您的网络中搜索 Brother 产品，查看状态并配置网络设置。不同于专为 Windows® 设计的 BRAdmin 专业版 3， WebBRAdmin 是一种基于服务器的实用程序，可在任何带有支持 JRE (Java 运行环境 ) 的网络浏览器的客户端计算机中访问。只需在运行 IIS 1 的计算机上安装 Web BRAdmin 服务器实用程序，即可连接到 Web BRAdmin服务器，然后与设备本身进行通信。

如需获取更多信息或下载相关资料，请访问以下网站：http://solutions.brother.com/。

1 因特网信息服务器 4.0 或因特网信息服务 5.0/5.1/6.0/7.0

# BRPrint Auditor ( 适用于 Windows®)

BRPrint Auditor 实用程序用于将 Brother 网络管理工具的监控能力应用到本地连接的设备上。通过该实用程序，客户端计算机可以收集通过 USB 接口与其相连的设备的使用和状态信息，然后由 BRPrint Auditor 将这些信息传递给网络上另一台运行 BRAdmin 专业版 3 或 Web BRAdmin 1.45 或更高版本的计算机，以便管理员能够检查页数统计、墨粉和硒鼓状态以及固件版本等项目。除了向 Brother 网络管理应用程序报告外，该实用程序还可以将使用和状态信息以 CSV 或 XML 文件格式通过电子邮件直接发送到预定的电子邮件地址( 需要 SMTP 邮件支持 )。 BRPrint Auditor 实用程序也支持电子邮件通知功能，用于显示警告和错误状况。

# 网络基本管理 ( 网络浏览器 )

网络基本管理 ( 网络浏览器 ) 是一个通过使用 HTTP ( 超文本传输协议 ) 管理网络中的 Brother 设备的实用程序。该实用程序通过使用安装在计算机上的标准网络浏览器可以查看网络中 Brother 设备的状态以及配置设备和网络设置。

如需获取更多信息，请参考第10 章: 网络基本管理。

增强了安全性的网络基本管理也支持 HTTPS。如需获取更多信息，请参考第 93 页上的安全管理网络打印机。

# 网络连接的类型

# 网络连接示例

# 使用 TCP/IP 协议的对等打印

在对等环境下，每台计算机直接向 / 从 Brother 设备发送 / 接收数据。不存在控制文件访问或打印机共享的中央服务器。

![对等打印配置示例：通过路由器直接连接多台计算机与Brother网络打印机，适合小型网络环境。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e52e357cf198d508cd23504d32dc4ae72b216e7e0e4d51e45070dee8211a5a85.jpg)

1) 路由器  
2) 网络打印机 ( 本设备 )

 在拥有 2 台或 3 台计算机的小型网络环境中， Brother 建议您采用对等打印方式，因其比网络共享打印方式更易于配置。请参考第 5页上的网络共享打印。  
 每台计算机必须使用 TCP/IP 协议。  
 Brother 设备需要配置合适的 IP 地址。  
 如果使用路由器，则必须在计算机和 Brother 设备中配置网关地址。

# 网络共享打印

在网络共享环境下，所有计算机都需要通过中央控制计算机发送数据。这类计算机通常称为 “ 服务器 ” 或“ 打印服务器 ”。其作用是控制所有打印作业的打印。

![网络共享打印配置：客户端通过服务器连接打印机，支持TCP/IP或USB接口。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6684be3cb4e508888c34ac8981c63b0b99e41d1d80ac0d36e72ea5bedecef9e9.jpg)

1) 客户端计算机  
2) 也称为 “服务器 ” 或 “打印服务器 ”  
3) TCP/IP 或 USB 接口电缆   
4) 打印机 ( 本设备 )

 在大型网络环境中， Brother 建议您使用网络共享打印方式。  
 “ 服务器 ” 或 “ 打印服务器 ” 必须使用 TCP/IP 打印协议。  
 若设备并非通过服务器上的 USB 接口连接，则需要为 Brother 设备配置合适的 IP 地址。

# 无线网络连接示例 ( 适用于 HL-3070CW)

# 通过网络中的接入点连接至计算机 ( 基础架构模式 )

此种类型的网络中心具有一个中央接入点。接入点也可以作为连接有线网络的网桥或网关。当 Brother 无线设备 (本设备 ) 接入网络时，它将通过接入点接收所有打印作业。

![基础架构模式网络示意图：展示接入点、无线打印机及有线/无线计算机的连接方式。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/5bffdd8910600a1c1b6138cc49aa10611b7c3c1647771f1d0003a788d2c1b7ec.jpg)

1) 接入点  
2) 无线网络打印机 ( 本设备 )  
3) 连接至接入点的支持无线网络的计算机  
4) 通过以太网电缆连接至接入点的不支持无线网络的有线计算机

# 协议

# TCP/IP 协议和功能

协议是为在网络上传送数据设置的标准化规则，使用户能够访问连接网络的各种资源。

本 Brother 设备使用的打印服务器支持 TCP/IP 协议 ( 传输控制协议 / 因特网协议 )。

TCP/IP 是因特网、电子邮件等网络通信中应用最为广泛的协议，可应用于如 Windows®、 WindowsServer®、 Mac OS X 和 Linux® 等几乎所有的操作系统。本款 Brother 设备支持以下 TCP/IP 协议。

![Brother设备支持广泛使用的TCP/IP协议，适用于多种操作系统，并可通过HTTP接口配置设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6547c918ff6bea5fbfb5de09d13d89349abc0fbd9485e1a2216e8eb101e22963.jpg)

# 注释

• 您可以通过使用 HTTP 接口 ( 网络浏览器 ) 配置协议设置。  
请参考第76页上的如何使用网络基本管理 ( 网络浏览器) 配置打印服务器设置。  
• 关于安全协议的详细信息，请参考第 91 页上的安全协议。

# DHCP/BOOTP/RARP

通过使用 DHCP/BOOTP/RARP 协议，可自动配置 IP 地址。

![打印服务器设置：介绍如何通过DHCP/BOOTP/RARP协议自动配置IP地址及APIPA的使用条件。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/de45d459d32d30bfcfa4c9cdf3b4b1451c72a7a4457ecbaa05f024b172a220d2.jpg)

# 注释

若要使用 DHCP/BOOTP/RARP 协议，请联系您的网络管理员。

# APIPA

如果您未手动 ( 使用设备的操作面板或 BRAdmin 应用程序 ) 或自动 ( 使用 DHCP/BOOTP/RARP 服务器 ) 指定 IP 地址，则自动专用 IP 寻址 (APIPA) 协议将在 169.254.1.0 至 169.254.254.255 范围内自动指定 IP 地址。

# ARP

地址解析协议在 TCP/IP 网络中将 IP 地址映射到 MAC 地址。

# DNS 客户端

Brother 打印服务器支持域名系统 (DNS) 客户端功能。该功能允许打印服务器使用 DNS 名称与其他设备进行通信。

# NetBIOS 名称解析

通过使用网络基本输入 / 输出系统 (NetBIOS) 名称解析，您可以在进行网络连接时通过其他设备的 NetBIOS名称获得其 IP 地址。

# WINS

Windows 因特网名称服务信息通过合并 IP 地址和本地网络中的 NetBIOS 名称为 NetBIOS 名称解析提供服务。

# LPR/LPD

在 TCP/IP 网络中广泛应用的打印协议。

# SMTP 客户端

简单邮件传输协议 (SMTP) 客户端通过因特网或内部网发送电子邮件。

# 自定义原始端口 (Custom Raw Port) ( 默认为 Port9100)

另一个在 TCP/IP 网络中广泛应用的打印协议。该协议实现了交互式数据传输。

# IPP

因特网打印协议 (IPP 版本 1.0) 允许通过因特网直接将文档打印至任何可访问的打印机上。

![介绍IPP协议支持互联网直接打印及mDNS协议让Brother打印服务器在Mac OS X中自动配置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b7a5d108449dc61a879c866e782d0c3594a92e8a8f87ac348001256184ff5439.jpg)

# 注释

关于 IPPS 协议，请参考第 91页上的安全协议。

# mDNS

mDNS 允许 Brother 打印服务器在 Mac OS X 简单网络配置系统中自动进行工作配置。(Mac OS X 10.3.9 或更高版本 )。

# Telnet

Brother 打印服务器支持 Telnet 服务器的命令行配置。

# SNMP

简单网络管理协议 (SNMP) 用于管理计算机、路由器和 Brother 网络设备等网络设备。Brother 打印服务器支持 SNMPv1、 SNMPv2c 和 SNMPv3。

![SNMP协议介绍及Brother打印服务器支持版本，提及SNMPv3详情见第91页，并简述LLMNR作用。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/aec29cde4f1eeb6fe34c1e787b2263d2f8dd06266d86b661ecf5f4613e7c3723.jpg)

# 注释

关于 SNMPv3 协议，请参考第 91页上的安全协议。

# LLMNR

如果网络中没有域名系统 (DNS) 服务器，则由链路局部多播名称解析协议 (LLMNR) 确定邻接计算机的名称。当使用具有 LLMNR 发送器功能的计算机 ( 如 Windows Vista® 和 Windows® 7 系统 ) 时， LLMNR 应答器功能可作用于 IPv4 或 IPv6 环境。

# 网络服务

通过使用网络服务协议，Windows Vista® 和 Windows® 7 用户只需要右击网络文件夹中的设备图标即可安装Brother 打印机驱动程序。

请参考第 135 页上的使用网络服务时的安装 ( 适用于 Windows Vista® 和 Windows® 7 用户 )。

网络服务同时也可在计算机中查看设备的当前状态。

# 网络服务器 (HTTP)

内置有网络服务器的 Brother 打印服务器可允许您使用网络浏览器监控其状态或更改一些配置设置。

![Brother打印服务器内置网络服务，支持通过浏览器监控状态和修改配置。建议使用IE 6.0或Firefox 1.0以上版本访问。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/156ab4d704c95f405fa2ee9f5d4adcf2f37b8a9dfca287cafb3917a68a3a9d76.jpg)

# 注释

• Brother 建议 Windows® 用户使用 Microsoft® Internet Explorer® 6.0 ( 或更高版本 ) 或 Firefox 1.0 ( 或更高版本 )， Macintosh 用户使用 Safari 1.3 ( 或更高版本 )。无论使用何种浏览器，请确保始终启用JavaScript 和 Cookies。如果使用其他网络浏览器，请确保其与 HTTP 1.0 和 HTTP 1.1 兼容。  
• 关于 HTTPS 协议，请参考第 91 页上的安全协议。

# IPv6

本设备兼容下一代因特网协议 IPv6。关于 IPv6 协议的更多信息，请访问以下网站：

http://solutions.brother.com/。

# 其他协议

# LLTD

通过使用链路层发现协议 (LLTD)，您可以在 Windows Vista® 和 Windows® 7 网络映射中轻松定位 Brother 设备。将以一个明显图标和节点名称显示您的 Brother 设备。此协议的默认设置为关闭。您可以使用 BRAdmin专业版 3 实用程序激活 LLTD。请通过登录以下网站：http://solutions.brother.com/ 在下载页面中下载适用于您的产品型号的 BRAdmin 专业版 3。

# 2 配置网络设备

# 概述

在网络上使用 Brother 设备之前，您必须在设备上安装 Brother 软件并配置正确的 TCP/IP 网络设置。在本章中，您将了解通过使用 TCP/IP 协议的网络进行打印所需的基本步骤。

Brother 建议您使用随机光盘上的 Brother 安装程序安装 Brother 软件。它将指导您完成软件和网络安装。请遵循随机附带的快速安装指南的说明进行安装。

![Brother打印机网络设置：推荐使用安装程序，也可手动通过操作面板更改设置。详见第53页网络菜单。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9fb9a9dcf286b68b8dc4f42ae83b887e77dbcf3a96491ee23044dd580288aa6e.jpg)

# 注释

如果您不想或无法使用自动安装程序或任何 Brother 软件工具，您也可以使用设备的操作面板更改网络设置。

如需获取更多信息，请参考第 53页上的网络菜单。

# IP 地址、子网掩码和网关

若要在 TCP/IP 网络环境下使用本设备，您必须配置 IP 地址和子网掩码。分配到打印服务器的 IP 地址必须与主机处于同一逻辑网络中。否则，您必须正确配置子网掩码和网关地址。

# IP 地址

IP 地址为一系列数字，用于识别接入网络的各台装置。每个 IP 地址由 4 组数字组成，并由点来分隔。每组数字必须在 0 至 255 之间。

 例如：在小型网络中，通常只需要更改最后一组数字即可设置 IP 地址。

• 192.168.1.1   
• 192.168.1.2   
• 192.168.1.3

# 如何将 IP 地址分配至打印服务器：

如果在您的网络中有 DHCP/BOOTP/RARP 服务器 ( 通常为 UNIX®、 Linux 或 Windows® 2000/XP、

Windows Vista®、 Windows® 7 或 Windows Server® 2003/2008 网络 )，打印服务器将从服务器中自动获取IP 地址。

![在支持的Windows系统网络中，打印服务器通过DHCP自动获取IP地址；小型网络可使用路由器作为DHCP服务器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/0550f791af58f9d6d4c67ed0e259d34630697219c0d6c66bdc509cdbdf3b7ff8.jpg)

# 注释

在小型网络中， DHCP 服务器可以为路由器。

关于 DHCP、 BOOTP 和 RARP 的详细信息，请参考：

第 128 页上的使用 DHCP 配置 IP 地址

第 129 页上的使用 BOOTP 配置 IP 地址

第 130 页上的使用 RARP 配置 IP 地址。

如果不存在 DHCP/BOOTP/RARP 服务器，自动专用 IP 寻址 (APIPA) 协议将在 169.254.1.0 至

169.254.254.255 范围内自动指定 IP 地址。关于 APIPA 的详细信息，请参考第 130 页上的使用 APIPA 配置IP 地址。

如果禁用 APIPA 协议，Brother 打印服务器的默认 IP 地址为 192.0.0.192。但您可以方便地将 IP 地址更改为与您网络相匹配的 IP 地址。关于如何更改 IP 地址的详细信息，请参考第 13 页上的设置 IP 地址和子网掩码。

# 子网掩码

子网掩码限制网络通信。

 例如：计算机 1 可以与计算机 2 通信

• 计算机 1

IP 地址：192.168. 1. 2

子网掩码：255.255.255.000

• 计算机 2

IP 地址：192.168. 1. 3

子网掩码：255.255.255.000

子网掩码中的 0 表示在这部分地址中无通信限制。在上例中，我们可以与任何以 192.168.1.x (x. 为 0 至 255之间的数字) 开始的 IP 地址的设备进行通信。

# 网关 ( 和路由器 )

网关是进入其他网络的网络节点，可以通过网络将传输数据发送至准确目的地。路由器可确认在网关上数据传输的路径。如果目的地处于外部网络，路由器就会将数据传输至外部网络。如果您的网络要与其他网络进行通信，您可能需要配置网关 IP 地址。如果您不确定网关的 IP 地址，请联系您的网络管理员。

# 步骤流程图

# 配置 TCP/IP 设置。

o 配置 IP 地址 请参考第 13 页  
o 配置子网掩码 请参考第 13 页  
o 配置网关 请参考第 13 页

# b 更改打印服务器设置。

o 使用 BRAdmin Light 实用程序 请参考第 16 页  
o 使用 BRAdmin 专业版 3 实用程序 请参考第 16 页  
o 使用网络基本管理 ( 网络浏览器) 请参考第 17 页  
o 使用操作面板 请参考第 17页  
o 使用其他方式 请参考第 17 页

# 设置 IP 地址和子网掩码

# 使用 BRAdmin Light 实用程序配置网络打印机

# BRAdmin Light

BRAdmin Light 是一个用于为连接网络的 Brother 设备进行初始设置的实用程序。它也可以在 TCP/IP 环境下搜索 Brother 产品，查看状态并配置如 IP 地址等基本网络设置。可以在 Windows® 2000/XP、 WindowsVista®、 Windows® 7、 Windows Server® 2003/2008 和 Mac OS X 10.3.9 或更高版本的操作系统下使用BRAdmin Light 实用程序。

# 如何使用 BRAdmin Light 实用程序配置本设备

![如何在不同操作系统下使用BRAdmin Light配置设备及获取该软件的方法。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/727ba5cea3b648c5849690ed8833b29d1a41d628e1c673dc95450bde2be180db.jpg)

# 注释

• 请使用 Brother 产品随机光盘中的 BRAdmin Light 实用程序。您也可以登录以下网站：http://solutions.brother.com/ 下载最新版本的 Brother BRAdmin Light 实用程序。  
• 如果需要更高级的打印机管理，可以登录以下网站：http://solutions.brother.com/ 下载最新版本的BRAdmin 专业版 3 实用程序。该实用程序仅适用于 Windows® 用户。  
• 如果您正在使用反间谍软件或防病毒应用程序的防火墙功能，请暂时将其禁用。一旦您确认可以进行打印，请遵循相关说明配置软件设置。  
• 节点名称：节点名称显示于当前 BRAdmin Light 窗口中。本设备打印服务器的默认节点名称为“BRNxxxxxxxxxxxx” ( 有线网络 ) 或 “BRWxxxxxxxxxxxx” ( 无线网络 )。 (“xxxxxxxxxxxx” 为本设备的MAC 地址 / 以太网地址。 )  
• Brother 打印服务器的默认密码为 “access”。

启动 BRAdmin Light 实用程序。

 Windows® 用户

点击开始 / 所有程序 1/Brother/BRAdmin Light/BRAdmin Light。

1 对于 Windows® 2000 用户，此处为程序

 Macintosh 用户

双击 Macintosh HD ( 硬盘 )/Library ( 资源库 )/Printers ( 打印机 )/Brother/Utilities ( 实用程序 )/BRAdmin Light.jar 文件。

b BRAdmin Light 将自动搜索新设备。

# c 双击未配置设备。

Windows®   
![BRAdmin Light自动搜索新设备，双击未配置设备以开始设置。支持Windows和Mac系统。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/463b34b2569a7b27a54db3f3cf4fbdf77de60889d7479a85103192cabbaad961.jpg)

Macintosh   
![Macintosh电脑设置网络打印服务器的界面示意图。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bf6d23f520243a2b85bda6910039a02b68bff7cea7c3c1fc9cd9000c4eefd1d7.jpg)

![Macintosh系统下使用BRAdmin Light实用程序检测网络打印机状态的示意图。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/321ac812ddf77bd9b65e1295b401772ab166cee47fa2c05ff4d6fa612dd73f24.jpg)

# 注释

• 如果打印服务器设置为出厂默认设置 ( 如果未使用 DHCP/BOOTP/RARP 服务器 )，在 BRAdmin Light实用程序屏幕上设备将显示为未配置。  
• 通过打印网络配置页，您可以查找到节点名称和 MAC 地址 ( 以太网地址 )。  
请参考第 68 页上的打印网络配置页。

# d 在引导方式中选择 STATIC。输入打印服务器的 IP 地址、子网掩码和网关 ( 如有需要 )。

Windows®   
![设置打印服务器静态IP地址、子网掩码及网关的步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e322a101a1705b2ec1503f9016c2df9824f1d2f1a4e26619187552e2561418a9.jpg)

Macintosh   
![Macintosh系统下，通过输入正确的IP地址，在设备列表中显示Brother打印服务器的步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e6e9649e2f6e13634644934640eb4d490a1b271202987dcad36f45bcbcfdaace.jpg)

e 点击确定。  
f 输入正确的 IP 地址，设备列表中将显示 Brother 打印服务器。

# 使用操作面板配置网络设备

您可以使用操作面板上的 Network ( 网络 ) 菜单配置网络设备。

请参考第 53 页上的网络菜单。

# 使用其他方式配置网络设备

您可以使用其他方式配置网络设备。

请参考第 128 页上的设置 IP 地址的其他方法 ( 适用于高级用户和管理员 )。

# 更改打印服务器设置

![配置网络设备的其他方法及更改打印服务器设置指南，包括无线网络设置和使用BRAdmin Light工具。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/47dcf5896402ee9faf6728da464b5b70d7e4c7df1c2a860d58c67824c0742497.jpg)

# 注释

无线网络用户需要配置无线设置以更改打印服务器设置。请参考第 3 章的配置无线网络设备 ( 适用于 HL-3070CW)。

# 使用 BRAdmin Light 实用程序更改打印服务器设置

启动 BRAdmin Light 实用程序。

 Windows® 用户

点击开始 / 所有程序 1/Brother/BRAdmin Light/BRAdmin Light。

1 对于 Windows® 2000 用户，此处为程序

 Macintosh 用户

双击 Macintosh HD ( 硬盘 )/Library ( 资源库 )/Printers ( 打印机 )/Brother/Utilities ( 实用程序 )/BRAdmin Light.jar 文件。

b 选择您想更改设置的打印服务器。  
c 从控制菜单中选择网络配置。  
d 输入密码。默认密码为 “access”。  
e 此时可以更改打印服务器设置。

![更改打印服务器网络配置步骤及高级设置获取方式说明](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/69438e5c4cceb7e6d3b5c77b2a37a88cb44df968cf221b399f10909fe0d11fa8.jpg)

# 注释

如果您想更改更多高级设置，请登录以下网站：http://solutions.brother.com/ 下载 BRAdmin 专业版 3 实用程序 ( 仅适用于 Windows®)。

# 使用 BRAdmin 专业版 3 实用程序更改打印服务器设置 ( 适用于 Windows®)

![使用BRAdmin专业版3实用程序更改打印服务器设置，仅适用于Windows®，请从官网下载最新版本。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9f919a2c5fa21fe3d840ca94a709d948708a135e255585a82ab6d69725f30e5a.jpg)

# 注释

• 请使用最新版本的 BRAdmin 专业版 3 实用程序，可登录以下网站下载：http://solutions.brother.com/。该实用程序仅适用于 Windows® 用户。  
• 如果您正在使用反间谍软件或防病毒应用程序的防火墙功能，请暂时将其禁用。一旦您确认可以进行打印，请遵循相关说明配置软件设置。  
• 节点名称：节点名称显示于当前 BRAdmin 专业版 3 窗口中。本设备打印服务器的默认节点名称为“BRNxxxxxxxxxxxx” ( 有线网络 ) 或 “BRWxxxxxxxxxxxx” ( 无线网络 )。 (“xxxxxxxxxxxx” 为本设备的MAC 地址 / 以太网地址。 )

a ( 从 Windows® 操作系统 ) 点击开始 / 所有程序 1/Brother Administrator Utilities/Brother BRAdminProfessional 3/BRAdmin Professional 3 以启动 BRAdmin 专业版 3 实用程序。

1 对于 Windows® 2000 用户，此处为程序

![BRAdmin专业版3启动指南及打印服务器配置步骤，包括选择设备、配置设置和输入密码等。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4a691caac993da7e2945ed3024186a05a288dc60680e5e4625111e704c174e14.jpg)

b 选择您想配置的打印服务器。  
c 从控制菜单中选择配置设备。  
d 如果您已设置密码，请输入您的密码。默认密码为 “access”。  
e 此时可以更改打印服务器设置。

![配置打印服务器步骤：选择设备、配置设置、输入密码（默认"access"）、更改设置。未使用DHCP时，设备显示为"APIPA"。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e7dd729588b6100d675cc6b742a03764594701c3838a3f24390cf095e5345d02.jpg)

# 注释

• 如果未使用 DHCP/BOOTP/RARP 服务器将打印服务器设置为出厂默认设置，在 BRAdmin 专业版 3 实用程序屏幕上设备将显示为 "APIPA"。  
• 通过打印网络配置页，您可以查找到节点名称和 MAC 地址 / 以太网地址 ( 上述 IP 地址 )。请参考第 68 页上的打印网络配置页。

# 使用网络基本管理 ( 网络浏览器 ) 更改打印服务器设置

可通过标准网络浏览器更改使用 HTTP (超文本传输协议 ) 的打印服务器设置。

请参考第76页上的如何使用网络基本管理 ( 网络浏览器) 配置打印服务器设置。

# 使用操作面板更改打印服务器设置

您可以使用操作面板上的 Network ( 网络 ) 菜单配置和更改打印服务器设置。

请参考第 53 页上的网络菜单。

# 使用其他方式更改打印服务器设置

您可以使用其他方式配置网络打印机。

请参考第 128 页上的设置 IP 地址的其他方法 ( 适用于高级用户和管理员 )。

# 3 配置无线网络设备 ( 适用于 HL-3070CW)

# 概述

若要将打印机连接至无线网络，您需要执行快速安装指南或网络使用说明书中的相关步骤。 Brother 建议您使用随机光盘上的 Brother 安装程序。使用此应用程序，可简便地将设备连接至无线网络，并安装完成无线网络设备配置所需的网络软件和打印机驱动程序。屏幕提示将指导您如何配置，直至您可以使用 Brother 无线网络设备。

如果您想在不使用 Brother 安装程序的情况下配置打印机，请仔细阅读本章中关于如何配置无线网络设置的详细信息。关于 TCP/IP 设置的详细信息，请参考第 13 页上的设置 IP 地址和子网掩码。关于使用操作面板菜单中的 SecureEasySetup、Wi-Fi Protected Setup 或 AOSS™ 的无线配置，请参考第 6 章。关于使用 Wi-Fi Protected Setup 的 PIN 方式的无线配置，请参考第 7 章。

![无线配置指南及打印机放置建议，确保靠近路由器减少干扰。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/cad3c30400f74559ce1782acff5114d8ef5136c0b82da424e089d55e5d61f1d8.jpg)

# 注释

• 为实现日常文档打印的最佳效果，请将 Brother 设备放置在尽量靠近网络接入点/ 路由器的地方，并尽量减少中间的障碍物。两设备间的大型物体和墙壁以及来自其他电气设备的干扰都可能会影响文档数据传输速度。  
由于上述因素的限制，无线连接并非是所有类型文档和应用程序的最佳连接方式。若要打印大量文件，如带有混合文本和大量图片的多页文档，则可以选择能够更快速传输数据的有线以太网连接或具有最快处理速度的 USB 连接。  
• 尽管 Brother 设备可应用于有线和无线网络，但每次仅可应用一种连接方式。

# 无线网络术语和概念

如果您想在无线网络中使用本设备，则必须确保配置的设备与现有的无线网络设置相匹配。本部分提供几个关于此设置的主要术语和概念，在配置无线网络设备时可能会有所帮助。

# SSID ( 服务区标识符 ) 和信道

需要配置 SSID 和信道以指定要连接的无线网络。

# SSID

每个无线网络都有其专有的网络名称，技术上称为 SSID 或 ESSID (扩展服务区标识符 )。SSID 是一个将被分配到接入点的不超过 32 个字节的数值。要连接至无线网络的无线网络设备应与接入点相匹配。接入点和无线网络设备定期发送带有 SSID 信息的无线分组 (通常称为信标 )。当您的无线网络设备接收信标时，您可以识别其无线电波能够到达设备的最近无线网络。

# 信道

无线网络需使用信道。每个无线信道处于不同的频率。使用无线网络时，共有 14 个不同的信道可供使用。但很多国家都限制可用信道的数量。如需获取更多信息，请参考第 137页上的无线网络 ( 适用于 HL-3070CW)。

# 验证和加密

大多数无线网络会采用某种安全设置。这些安全设置确定验证 ( 如何在网络中识别设备 ) 和加密 ( 如何在网络上发送数据时将其加密 )。配置 Brother 无线设备时如未正确指定这些选项，则将无法连接到无线网络。因此，在配置这些选项时务必多加注意。请参考以下信息以查看您的 Brother 无线设备所支持的验证和加密方式。

# 验证方式

Brother 设备支持以下方式：

 开放系统

允许无线设备在未经过任何验证的情况下接入网络。

 共享密钥

所有访问无线网络的设备都共享一个保密预设密钥。 Brother 设备使用 WEP 密钥作为预设密钥。

 WPA-PSK/WPA2-PSK

启用 Wi-Fi 保护接入预共享密钥 (WPA-PSK/WPA2-PSK)，它通过使用 WPA-PSK 的 TKIP 或 WPA-PSK的 AES 以及 WPA2-PSK 加密 (WPA-Personal) 将 Brother 无线设备与接入点进行连接。

 LEAP

Cisco LEAP ( 轻度扩展验证协议 ) 由思科系统公司研发，使用用户 ID 和密码进行验证。

#  EAP-FAST

EAP-FAST (扩展验证协议 - 通过安全隧道的灵活验证 ) 由思科系统公司研发，是使用用户 ID 和密码进行验证、通过对称密钥算法实现隧道验证的过程。

Brother 设备支持以下内部验证：

• EAP-FAST/ 无

适用于 CCXv3 网络的 EAP-FAST 验证。不使用内部验证方式。

• EAP-FAST/MS-CHAPv2

适用于 CCXv4 网络的 EAP-FAST 验证。使用 MS-CHAPv2 作为内部验证方式。

• EAP-FAST/GTC

适用于 CCXv4 网络的 EAP-FAST 验证。使用 GTC 作为内部验证方式。

# 加密方式

加密功能用于保护通过无线网络发送的数据。 Brother 设备支持以下加密方式：

 无

未使用任何加密方式。

 WEP

通过使用 WEP ( 有线等效加密 )，以安全密钥发送和接收数据。

 TKIP

TKIP ( 暂时密钥集成协议) 提供融合信息完整性检查和密钥更新机制的每包密钥。

 AES

AES ( 高级加密标准 ) 是 Wi-Fi 授权加强加密标准。

 CKIP

思科系统公司的 LEAP 的原始密钥完整性协议。

# 网络密钥

每种安全方式都有其规则：

 开放系统 /WEP 共享密钥

此密钥是必须以 ASCII 或十六进制格式输入的 64 位或 128 位的数值。

• 64 (40) 位 ASCII：  
使用 5 个文本字符。例如：“WSLAN” ( 区分大小写 )。

• 64 (40) 位十六进制值：

使用 10 位十六进制数据。例如：“71f2234aba”。

• 128 (104) 位 ASCII：  
使用 13 个文本字符。例如：“Wirelesscomms” ( 区分大小写 )。  
• 128 (104) 位十六进制值：  
使用 26 位十六进制数据。例如：“71f2234ab56cd709e5412aa2ba”。

 WPA-PSK/WPA2-PSK 和 TKIP 或 AES

使用长度介于 8 至 63 个字符之间的预共享密钥 (PSK)。

 LEAP

使用用户 ID 和密码。

• 用户 ID：长度少于 64 个字符。  
• 密码：长度少于 32 个字符。

 EAP-FAST

使用用户 ID 和密码。

• 用户 ID：长度少于 64 个字符。  
• 密码：长度少于 32 个字符。

# 无线网络配置步骤流程图

# 基础架构模式

a 确认您的网络环境。 ( 请参考第 23 页。 )

o 基础架构模式

连接至带有一个接入点的计算机

![无线网络配置流程：确认网络环境与设置方式，选择基础架构模式连接至接入点。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8b2cd96e6fba7b5fa63be9e285d757624b49f8af32551f9209cc5a17e57bd6db.jpg)

b 确认您的无线网络设置方式。 ( 请参考第 24 页。 )

![确认无线网络设置方式并配置无线网络设备的步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6d4d301e7561749496e0379efc62508fd36155e7a1a5276545fd084e3c69ad37.jpg)

c 配置无线网络设备。 ( 请参考第 27 页。 )

![配置无线网络设备并完成打印机驱动安装，确认网络环境及通过接入点连接计算机。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c3d9f479e079da8e1b710fbaf276d5d6f4964a12f558b74d27b9c4075b425048.jpg)

确定！ 已完成无线配置和打印机驱动程序的安装。

# 确认您的网络环境

# 通过网络中的接入点连接至计算机 ( 基础架构模式 )

![无线网络打印机通过接入点与计算机（无线/有线）连接的示意图及设置确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ad785f95960e6122d61502d5192a472a3a03910a97245988c56f2bab09ee4f35.jpg)

1) 接入点  
2) 无线网络打印机 ( 本设备 )  
3) 连接至接入点的支持无线网络的计算机  
4) 通过以太网电缆连接至接入点的不支持无线网络的有线计算机

# 确认无线网络设置方式

共有三种配置无线网络设备的方式：使用随机光盘上的 Brother 安装程序 (推荐 )、使用一键式无线设置模式和使用 Wi-Fi Protected Setup 的 PIN 方式。设置过程因网络环境的不同而有所不同。

# 使用随机光盘上的 Brother 安装程序配置无线网络设备 ( 推荐 )

Brother 建议您使用随机光盘上的 Brother 安装程序。使用此应用程序，可简便地将设备连接至无线网络，并安装完成无线网络设备配置所需的网络软件和打印机驱动程序。屏幕提示将指导您如何配置，直至您可以使用 Brother 无线网络设备。在进行此安装前必须了解您的无线网络设置。

# 临时使用 USB 或网络电缆的配置

您可以临时使用 USB 接口电缆或网络电缆配置本 Brother 设备的无线网络设置。

# USB 方法 ( 适用于 Windows®)

 您可以使用 USB 电缆 (A) 从同一网络中的计算机远程配置本设备。

![使用USB或以太网电缆配置Brother设备的无线网络设置方法。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/93abc97554b4f7475101c045ab4c5aa4e89cb2dd580b5f665cba8028761410f3.jpg)

# 以太网电缆方式 ( 适用于 Macintosh)

 如果同一网络中有以太网集线器或路由器作为无线局域网的接入点 (A)，您可以临时使用网络电缆 (B) 将集线器或路由器连接至设备。随后，您便可以在接入网络的计算机上远程配置本设备。

![使用网线临时连接设备与集线器/路由器进行远程配置，或通过SES/WPS、AOSS配置无线网络。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a094d39aaae23fe1724e82ecdbc9abe12a3ac3760757fdcff1991d95fbeeb67d.jpg)

# 使用操作面板菜单中的 SES/WPS 或 AOSS 配置无线网络设备 ( 仅适用于基础架构模式 )

如果无线接入点 (A) 支持 SecureEasySetup、 Wi-Fi Protected Setup (PBC 1) 或 AOSS™，则可以不使用计算机而进行设备的配置。

![使用SecureEasySetup、Wi-Fi Protected Setup或AOSS™技术，无需计算机即可配置设备；介绍Push Button和PIN方式配置无线网络。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b7c52fe5feab4223710d80d9a6aae2885dc894768e92c3cfe7e6dfe80bf9bc58.jpg)

1 Push Button 配置

# 使用 Wi-Fi Protected Setup 的 PIN 方式配置无线网络设备 ( 仅适用于基础架构模式 )3

如果您的无线接入点 (A) 支持 Wi-Fi Protected Setup，则您可以使用 Wi-Fi Protected Setup 的 PIN 方式进行配置。 ( 请参考第 7 章的使用 Wi-Fi Protected Setup 的 PIN 方式的无线配置 ( 适用于 HL-3070CW)。 )

 以注册构件 1 加强无线接入点 ( 路由器 ) (A) 的连接。

![使用Wi-Fi Protected Setup的PIN方式连接无线接入点与设备的示意图。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b239d9023ae4699e765e53b26d448f2dd2c70986d47116ae1f95d8cbdbb2e105.jpg)

 将计算机等其他设备 (C) 作为注册构件 1 时的连接。

![示例设备作为注册构件1连接至无线LAN的配置图，推荐使用Brother安装程序进行设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/dc634fd8c9874bf969dcd5d18426f7392529926550d13577878754a373739deb.jpg)

1 注册构件是用于管理无线 LAN 的设备。

# 配置无线网络设备

# 使用随机光盘上的 Brother 安装程序配置无线网络设备 ( 推荐 )

关于安装的详细信息，请参考第4 章的使用 Brother 自动安装程序进行的 Windows® 系统下的无线配置 ( 适用于HL-3070CW)或第5章的使用Brother安装程序进行的Macintosh系统下的无线配置（适用于HL-3070CW)。

# 使用操作面板菜单中的 SES/WPS 或 AOSS 配置无线网络设备

关于安装的详细信息，请参考第6 章的 3使用操作面板上的 SES/WPS 或 AOSS 进行的无线配置 ( 适用于HL-3070CW)。

# 使用 Wi-Fi Protected Setup 的 PIN 方式配置无线网络设备

关于安装的详细信息，请参考第 7 章的使用 Wi-Fi Protected Setup 的 PIN 方式的无线配置 ( 适用于 HL-3070CW)。

# 4

# 使用 Brother 自动安装程序进行的

# Windows® 系统下的无线配置

# ( 适用于 HL-3070CW)

# 在基础架构模式下进行的配置

# 配置无线设置之前

# 重要事项

本章阐述如何使用随机光盘上的适用于 Windows® 的 Brother 安装程序设置您的 Brother 设备。

如果您正在使用 Windows® XP，或者您目前使用的计算机已通过网络电缆连接至接入点 / 路由器，则您需要知道无线设定。

<table><tr><td>项目</td><td>记录无线网络的当前设置</td></tr><tr><td>SSID(网络名称)</td><td></td></tr><tr><td>网络密钥(安全密钥/加密密钥)</td><td></td></tr></table>

如已事先配置了打印机的无线设置，则必须将打印服务器恢复为出厂默认设置 ( 请参考第 67页上的将网络设置恢复为出厂默认设置)。

配置过程中需要临时使用 USB 接口电缆。

# 配置无线设置

将随机光盘插入 CD-ROM 光驱中。  
b 将自动显示打开屏幕。选择本设备和所需语言。  
c 出现随机光盘主菜单。点击安装打印机驱动程序。

![通过USB连接设备，使用随机光盘安装打印机驱动程序，并配置无线设置。若未自动运行，请手动启动start.exe。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/92a78a16d5848a130c471d2112494bf3a7004030087f3ef7a548f99a94d46ba6.jpg)

# 注释

• 如果未出现打开屏幕，请使用 Windows® 资源管理器运行 Brother 随机光盘根目录文件夹下的 start.exe程序。  
• 出现用户帐户控制屏幕时：$\ l ( \mathsf { W i n d o w s \lor i s t a } ^ { \otimes } )$ 点击允许。$( \mathsf { W i n d o w s } ^ { \otimes } 7 )$ 点击是。

d 点击无线网络用户。  
e 选择无线安装与驱动安装 (推荐 )，然后点击下一步。  
f 选择暂时使用 USB 接口电缆 (推荐 )，然后点击下一步。显示重要提示屏幕时，阅读重要提示。确认无线设置已启用后选中复选框，然后点击下一步。  
g 按照屏幕上的提示配置无线设置。

![通过USB连接配置无线设置，并继续安装打印机驱动程序。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/20d6950d9f386f1bb2e9033c71ee4fb2fc77859ad1f44b9a3426276d76eeeca2.jpg)

完成无线设置后，您可以继续进行打印机驱动程序安装。

请点击安装对话框中的下一步 ，然后按照屏幕上的提示执行操作。

# 5

# 使用 Brother 安装程序进行的 Macintosh 系统下的无线配置 ( 适用于 HL-3070CW)

# 在基础架构模式下进行的配置

# 配置无线设置之前

# 重要事项

本章阐述如何使用随机光盘上的适用于 Macintosh 的 Brother 安装程序设置您的 Brother 设备。

在进行此安装前必须了解您的无线网络设置。确保记录您无线网络环境的 SSID、安全验证和加密等所有当前设置。如果无法确定，请联系您的网络管理员或接入点 / 路由器的制造商。

<table><tr><td>项目</td><td>示例</td><td>记录无线网络的当前设置</td></tr><tr><td>通信模式:(基础架构模式)</td><td>基础架构模式</td><td></td></tr><tr><td>网络名称:(SSID、ESSID)</td><td>HELLO</td><td></td></tr><tr><td>验证方法:(开放系统、共享密钥、WPA-PSK $^{1}$ 、WPA2-PSK $^{1}$ 、LEAP、EAP-FAST)</td><td>WPA2-PSK</td><td></td></tr><tr><td>加密模式:(无、WEP、TKIP、AES、CKIP)</td><td>AES</td><td></td></tr><tr><td>网络密钥:(加密密钥、WEP 密钥 $^{2}$ 、密码)</td><td>12345678</td><td></td></tr></table>

WPA/WPA2-PSK 是 Wi-Fi 保护接入预共享密钥，它通过使用 TKIP 或 AES 加密 (WPA-Personal) 将 Brother 无线设备与接入点进行连接。WPA-PSK (TKIP 或 AES) 和 WPA2-PSK(AES) 使用长度介于 8 至 63 个字符之间的预共享密钥 (PSK)。

2 WEP 密钥适用于 64 位或 128 位加密网络，可同时包含数字和字母。如果您不确定此信息，请参考接入点或无线路由器附带的指导手册。此密钥是必须以 ASCII 或十六进制格式输入的 64 位或 128 位的数值。

# 例如：

64 位 ASCII： 使用 5 个文本字符。例如：“Hello” ( 区分大小写 )。

64 位十六进制值： 使用 10 位十六进制数据。例如：“71f2234aba”。

128 位 ASCII： 使用 13 个文本字符。例如：“Wirelesscomms” ( 区分大小写 )。

128 位十六进制值： 使用 26 位十六进制数据。例如：“71f2234ab56cd709e5412aa2ba”。

如已事先配置了打印机的无线设置，则必须将打印服务器恢复为出厂默认设置 ( 请参考第 67 页上的将网络设置恢复为出厂默认设置）。

如果您正在使用反间谍软件或防病毒应用程序的防火墙功能，请暂时将其禁用。一旦您确认可以进行打印，请遵循相关说明配置软件设置。

配置过程中需要临时使用以太网电缆。

# 配置无线设置

确保电源插头已经插上。  
b 启动设备，并等待设备进入准备就绪状态。  
c 启动 Macintosh。  
d 将随机光盘插入 CD-ROM 光驱中，双击桌面上的 HL3000 图标，然后双击 Start Here ( 点击此处开始 )图标。选择打印机型号和语言。  
e 出现随机光盘主菜单。点击安装打印机驱动程序。

![安装HL3000打印机驱动程序，选择无线网络用户选项。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b6b9f00d69c73d23b96bf729cad6d8e246dc7ea44ab31e5ed9d82744be0a169c.jpg)

f 点击无线网络用户。

![选择无线安装与驱动安装或仅有无线安装，点击下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d7c4e278da83df457d2c895eb528a09e554967b757c19d40bb87fcb1aa2752b1.jpg)

# g 选择无线安装与驱动安装 ( 推荐 ) 或仅有无线安装，然后点击下一步。

![选择无线安装与驱动安装或仅有无线安装，再选逐步安装，点击下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/dcc382f05ea96d8a0614af6b8ad3e8ad89075a80928fbafa3f76152c43c09c34.jpg)

# h 选择逐步安装 ( 推荐 )，然后点击下一步。

![选择逐步安装并点击下一步，然后选择带接口线并继续。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9891e8d83b7f33b74ae9ba808bf922bf76d7bde271a0e32b41c5b2f7c679a64b.jpg)

# i 选择带接口线 ( 推荐 )，然后点击下一步。

![选择带接口线连接方式，并用网线将网络接入点与Brother无线设备相连。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e58861190aceac81d1a3518be1be57c715ffd590c0b3d30d01f71289adebcf89.jpg)

j 用网络电缆连接您的网络接入点和 Brother 无线设备，然后点击下一步。

![使用网线连接网络接入点与Brother无线设备，选择并配置设备。确保设备开启并刷新列表。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/0e675d97e14c4c0acdc18a38b933f86d7f99ec799c0156c68438182c2983a3a5.jpg)

k 选择您想配置的设备，然后点击下一步。如果该表为空，查看接入点和设备是否已开启，然后点击刷新。

![选择并配置设备，检查接入点与设备状态，必要时点击刷新。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4f755ec2187fecd3a03d4879831cf6529a590be8561fa1df57ae0d41c200b18a.jpg)

![检查设备是否开启并点击刷新，显示网络中的可用设备列表。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/642b991dfe0bca8bc9428cb048f3569d4529c3a77a336c6c813234e5a432e103.jpg)

# 注释

• 默认节点名称为 “BRNxxxxxxxxxxxx”。  
• 通过打印网络配置页，您可以查找到打印机的 MAC 地址 ( 以太网地址 ) 和 IP 地址。请参考第 68 页上的打印网络配置页。

安装向导将搜索设备可以使用的无线网络。选择与设备相关联的接入点，然后点击下一步。

![安装向导搜索可用无线网络，选择接入点后继续设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c3ce164385e189691df0c22a822718951b87b90b2c8484cab9be9b1fb5480d1e.jpg)

![选择非"SETUP"的可用接入点，若无选项检查设备与接入点状态。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/73a9d2d14e5f918bad0308158e0f6375421bcafc7c8f69e5da8fb3a4210a4e7c.jpg)

# 注释

• “SETUP” 为设备的默认 SSID。请勿选择此 SSID。  
• 如果该表为空，查看接入点是否已开启并发送 SSID，然后查看设备和接入点是否处于无线通信的范围内。然后，点击刷新。  
• 如果接入点未设置为发送 SSID，则可以通过点击添加按钮进行手动添加。执行屏幕上的提示以输入名称 (SSID)，然后点击下一步。

![检查设备与接入点的无线连接范围，按提示操作添加未显示的SSID或继续设置无加密网络。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ea494b70eb133efd0e7a5e2e0073063546d62f079828cae7335a186a7083302c.jpg)

m 如果您的网络没有使用安全验证和加密，将出现以下屏幕。若要继续设置，点击运行，然后转到步骤o。

![根据网络是否使用安全验证和加密，显示不同设置屏幕，并指导用户如何继续配置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6f4ba7bdef5de6c40fffd20473f82da4225506a00d4c9b57720f9977eda4b275.jpg)

n 如果您的网络已使用安全验证和加密，将出现以下屏幕。配置 Brother 无线设备时，务必确保其配置与您在第 30 页中记录的已存在无线网络的安全验证和加密设置相匹配。从每个设置框的弹出菜单中选择验证方法和加密模式。输入网络密钥和确认网络密钥，然后点击下一步。

![配置无线设备时，选择验证方法、加密模式，并输入网络密钥。确保与已存在网络设置匹配。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/31449a32f6261f53ccde58abddc21145cc18bd76d6c8efc0f3d34e390be25e84.jpg)

![输入网络密钥并点击下一步，可选设置其他WEP密钥索引或联系管理员获取帮助。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/076d71339f5113fb3847c6b99e6b79fc44b436d293702e586486a38f6cd69a1d.jpg)

# 注释

• 如果除 WEP 密钥 1 之外您还想设置或配置其他 WEP 密钥索引，请点击高级。  
• 如果您不了解网络的安全验证或加密设置，请联系您的网络管理员或接入点 / 路由器制造商。  
• 如果您正在使用 WEP 且在步骤 o 中打印的网络配置页的 Wireless Link Status ( 无线连接状态 ) 项显示为 Link OK ( 连接完成 )，但在您的网络中没有找到本设备，请确认您已正确输入 WEP 密钥。 WEP密钥区分大小写。

o 点击下一步向设备提交下列设置。如果点击取消，设置则保持不变。设备将打印出网络配置页。

![输入WEP密钥后提交设置，或取消保持原设置并打印网络配置页。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/f91580c1133c3b8a6e53963324ec18d12c5013e74b375a938dddf52e231d0945.jpg)

![网络配置页示例，展示设备的当前网络设置信息。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/5d0e19ba79ad4414ca34772f151ba7fd972af495547402c8c9316f12814fdc41.jpg)

![设备网络设置界面，展示手动输入IP地址及无线设置提交后的WLAN启用状态。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/2cb66f3cc927f5e77599720a009ddc9abd7e343f0e26db0a46e758f2b47f4ec8.jpg)

# 注释

• 如果您想手动输入设备的 IP 地址设置，请点击变更 IP 地址，然后输入网络必需的 IP 地址设置。  
• 向设备提交无线设置后，操作面板设置自动变更为 WLAN Enable ( 启用无线网络)。

p 检查已打印的网络配置页。根据该页面中 Wireless Link Status ( 无线连接状态) 项显示的描述选择状态，然后点击下一步。

如果选择 "Link OK." ( 连接完成。 )，请转到步骤 r。

如果选择 "Failed To Associate" ( 连接失败 )，请转到步骤 q。

![根据连接状态选择下一步：成功则继续，失败则需重置设备并检查安全设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/45c3e03f32350afa48009f34ac5ba02dc538adda29fbfcbf77f2a8ea531ce3ab.jpg)

q 点击完成。无线设置失败是由于不正确的安全设置造成的，从而导致其无法与无线网络连接。请将打印服务器恢复为出厂默认设置 ( 请参考第 67页上的将网络设置恢复为出厂默认设置)。确认您的无线网络安全设置，并从步骤 f 开始重新设置。

![因安全设置问题无法连接无线网络时，恢复出厂设置并重新配置。断开设备与接入点连接后继续。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7ad49c7a8c69c41a43fb479f61c32d6ffd4078ff86de84c44b50afad6ca4ed96.jpg)

r 断开接入点 (集线器或路由器 ) 和设备的连线，并点击下一步或完成。

![断开设备与接入点的连接，完成无线设置步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7e26def3f60a33d3c96d8a4fd7f16a2a2ae979dfe69886276c734a48c19c4914.jpg)

![设备连线示意图及无线设置完成提示，含下一步操作指导。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/0da440a6b2c5a8ba5c07f5c060195bffcc45698e5b7d7eae581b55a35249fd6f.jpg)

无线设置已完成。如果您在步骤 g 中选择了安装打印机驱动程序，请按照屏幕上的提示执行操作。

# 6

# 使用操作面板上的 SES/WPS 或 AOSS 进行的无线配置

# ( 适用于 HL-3070CW)

# 概述

如果您的无线接入点 / 路由器支持 SecureEasySetup、Wi-Fi Protected Setup (PBC 1) 或 AOSS™，则无需知道无线网络设置即可轻松配置您的设备。本 Brother 设备的操作面板上有 SES/WPS/AOSS 菜单。此功能将自动检测您的接入点所要使用的模式 (SecureEasySetup、 Wi-Fi Protected Setup 或 AOSS™)。通过按无线接入点 / 路由器上的按钮，您可以设置无线网络和安全设置。关于如何进入一键式模式的详细信息，请参考无线接入点 / 路由器附带的使用说明书中的相关说明。

1 Push Button 配置

![支持一键设置功能的路由器或接入点图标示例，用于简化无线网络和安全配置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d7759a012e3c2720fac3fda2c16c1950c51fba68b65adc92dac189dbf1d027af.jpg)

# 注释

支持 SecureEasySetup、 Wi-Fi Protected Setup 或 AOSS™ 的路由器或接入点带有下图所示图标。

![支持SES、WPS或AOSS™功能的路由器图标示例。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/5cc0e492fe82ea4ca75eedb28238bf25cbb8fdf4682254513461dcc4465074c5.jpg)

![路由器或接入点的图标示例，展示设备连接状态与信号强度。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/fa0f5aa27885f4cb5ce0b17dc828b946d7cd0f33e9fa61b0d97ec54e51287775.jpg)

![Brother设备通过操作面板菜单使用SES/WPS或AOSS配置无线网络的步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4542622d899002b6a726829923462778187b3d7d94c3acbae3c692f9775e99f5.jpg)

# 如何使用操作面板菜单中的 SES/WPS 或 AOSS 配置无线设备

# 重要事项

若要将 Brother 设备连接至网络，Brother 建议您在安装前联系您的系统管理员。

如果您正在使用 Windows® 防火墙或反间谍软件或防病毒应用程序的防火墙功能，请暂时将其禁用。一旦您确认可以进行打印，请遵循相关说明配置软件设置。

如已事先配置了打印机的无线设置，则必须将打印服务器恢复为出厂默认设置 ( 请参考第 67 页上的将网络设置恢复为出厂默认设置)。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 SES/WPS/AOSS。按 OK ( 确定 ) 键。

![通过按键选择WLAN和SES/WPS/AOSS设置，支持Wi-Fi Protected Setup(PIN方式)配置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/cf8fb94b43f0686e53d0ac3307b9188209552739c81d1b9cd8ad8948da24d8eb.jpg)

# 注释

如果您的无线接入点支持 Wi-Fi Protected Setup (PIN 方式 )，而且您想使用 PIN ( 个人识别码 ) 方式配置您的设备，请参考第 43 页上的如何使用 Wi-Fi Protected Setup 的 PIN 方式配置无线设备。

e 设备搜索支持 SecureEasySetup、 Wi-Fi Protected Setup 或 AOSS™ 的接入点，将持续两分钟。  
f 根据接入点所支持的模式将接入点置于 SecureEasySetup 模式、Wi-Fi Protected Setup 模式或 AOSS™模式。请参考接入点附带的指导手册。

如果液晶显示屏上显示 Connected ( 已连接 )，则设备已成功连接至接入点 / 路由器。此时即可在无线网络中使用本设备。

如果液晶显示屏上显示 Connection Error ( 连接错误 )，则设备检测到会话重叠，即网络中同时有两个或以上的接入点 / 路由器启用 SecureEasySetup 模式、Wi-Fi Protected Setup 模式或 AOSS™ 模式。确保仅有一个接入点 / 路由器启用 SecureEasySetup 模式、 Wi-Fi Protected Setup 模式或 AOSS™ 模式，然后从步骤 a 开始重新设置。

如果液晶显示屏上显示 No Access Point ( 无接入点 )，则设备未在网络中检测到启用

SecureEasySetup 模式、Wi-Fi Protected Setup 模式或 AOSS™ 模式的接入点 / 路由器。请将设备移到更靠近接入点 / 路由器的地方，然后从步骤a 开始重新设置。

如果液晶显示屏上显示 Connection Fail ( 连接失败 )，则设备未成功连接至接入点 / 路由器。请从步骤 a 开始重新设置。如果再次显示相同信息，请将打印服务器恢复为出厂默认设置再重新进行设置 ( 关于如何恢复出厂默认设置，请参考第 67 页上的将网络设置恢复为出厂默认设置 )。

使用 SES/WPS/AOSS 操作面板菜单时的液晶显示屏信息

<table><tr><td>液晶显示屏信息</td><td>连接状态</td><td>操作</td></tr><tr><td>Setting WLAN(设置无线网络)</td><td>正在搜索或访问接入点,并从接入点下载设置。</td><td>-</td></tr><tr><td>Connecting SES(正在连接 SES)Connecting WPS(正在连接 WPS)Connecting AOSS(正在连接 AOSS)</td><td>正在连接接入点。</td><td>-</td></tr><tr><td>Connected(已连接)</td><td>连接成功。</td><td>-</td></tr><tr><td>Connection Error(连接错误)</td><td>检测到会话重叠。</td><td>确保仅有一个路由器或接入点启用SecureEasySetup 模式、Wi-Fi Protected Setup 模式或  $AOSS^{TM}$  模式,然后从步骤1开始重新设置。</td></tr><tr><td>No Access Point(无接入点)</td><td>接入点检测失败。</td><td>1 将设备移到更靠近接入点/路由器的地方,然后从步骤1开始重新设置。2 如果再次显示相同信息,请将打印服务器恢复为出厂默认设置再重新进行设置。</td></tr><tr><td>Connection Fail(连接失败)</td><td>连接失败。</td><td>1 请从步骤1开始重新设置。2 如果再次显示相同信息,请将打印服务器恢复为出厂默认设置再重新进行设置。</td></tr></table>

![网络连接失败时的解决步骤及无线网络安装完成后的驱动程序安装提示。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8ba73b38133a65f17d0c5c21610f587cb111162e361d7c3ff358a1e037c833d1.jpg)

( 对于 Windows®)

无线网络安装完成。如果您想继续安装运行设备必需的打印机驱动程序，请从随机光盘菜单中选择安装打印机驱动程序 。

( 对于 Macintosh)

无线网络安装已完成。如果您想继续安装运行设备必需的打印机驱动程序，请从随机光盘中选择Start Here OSX ( 按这里启动 OSX)。

# 7

# 使用 Wi-Fi Protected Setup 的 PIN 方式的无线配置

# ( 适用于 HL-3070CW)

# 概述

如果您的无线接入点 / 路由器支持 Wi-Fi Protected Setup (PIN 方式 )，则可以轻松进行设备的配置。PIN ( 个人识别码 ) 方式是由 Wi-Fi Alliance 开发的一种连接方式。通过将由 Enrollee ( 本设备 ) 创建的 PIN 输入到注册构件 ( 管理无线局域网的设备 )，您可以设置无线网络和安全设置。关于如何进入 Wi-Fi Protected Setup模式的详细信息，请参考无线接入点 / 路由器附带的使用说明书中的相关说明。

![支持Wi-Fi Protected Setup的设备图标，用于识别兼容设备。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ac7678182f570d540ec8e69e5fd638fccb8395a2f1e9edba9f0c6b65bbe17427.jpg)

# 注释

支持 Wi-Fi Protected Setup 的路由器或接入点带有下图所示图标。

![支持Wi-Fi Protected Setup的路由器图标，用于识别兼容设备。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d91f74d456317552f7e3eb57166ae3933a6f61c4ffe40d0f6fdab2be4c4e1900.jpg)

# 如何使用 Wi-Fi Protected Setup 的 PIN 方式配置无线设备

# 重要事项

若要将 Brother 设备连接至网络， Brother 建议您在安装前联系您的系统管理员。

确保电源插头已经插上。  
b 启动设备，并等待设备进入准备就绪状态。  
c 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
d 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
f 按 + 或 - 键选择 WPS w/PIN Code ( 有 PIN 密码的 WPS)。按 OK ( 确定 ) 键。  
液晶显示屏上将显示一个 8 位数的 PIN，然后设备开始搜索接入点，将持续五分钟。

h 使用网络中的计算机，然后在浏览器上输入 “http://access point’s IP address/”(“access point’s IPaddress” 是用作注册构件 1 的设备的 IP 地址 )。进入 WPS (Wi-Fi 保护设置 ) 设置页，然后将步骤 g 中液晶显示屏上显示的 PIN 输入注册构件并执行屏幕提示。

1 注册构件通常为接入点 / 路由器。

![通过输入设备液晶屏显示的PIN码，在接入点/路由器的WPS设置页完成Wi-Fi保护设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3f1bbd83fb3183d834f44e155c0a38963367a29fbf6f415b4e32cee82fecd550.jpg)

# 注释

设置页因接入点 / 路由器的不同而有所不同。请参考接入点 / 路由器附带的指导手册。

如果将 Windows Vista® 和 Windows® 7 系统下的计算机用作注册构件，请执行下列说明。

![设置Windows Vista®和Windows® 7系统计算机为网络注册构件的步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bae42d2fff807031a21ba6c64bed40a57c3427308bf6e1e00c2b305ffec06ce9.jpg)

# 注释

若要将 Windows Vista® 和 Windows® 7 系统下的计算机用作注册构件，需提前将其注册到网络中。请参考接入点/ 路由器附带的指导手册。

1 (Windows Vista®)

点击 按钮，然后点击网络。(Windows® 7)

点击 按钮 ，然后点击设备和打印机。

2 (Windows Vista®)点击添加无线设备。(Windows® 7)点击添加设备。

3 选择您的打印机，然后点击下一步。  
4 输入打印页上的 PIN，然后点击下一步。  
5 选择要连接的网络，然后点击下一步。  
6 点击关闭。

i 如果液晶显示屏上显示 Connected ( 已连接 )，则设备已成功连接至接入点 / 路由器。此时即可在无线网络中使用本设备。

如果液晶显示屏上显示 Connection Fail ( 连接失败 )，则设备未成功连接至接入点 / 路由器或输入的PIN 密码无效。请确认已输入正确的 PIN 密码，然后从步骤 f 开始重新设置。如果再次显示相同信息，请将打印服务器恢复为出厂默认设置再重新进行设置。关于如何恢复出厂默认设置，请参考第 67 页上的将网络设置恢复为出厂默认设置。

如果液晶显示屏上显示 No Access Point ( 无接入点 )，则设备未在网络中检测到接入点 / 路由器。请确保将 Brother 设备放置在尽量靠近网络接入点 / 路由器的地方，并尽量减少中间的障碍物，然后从步骤 f 开始重新设置。如果再次显示相同信息，请将打印服务器恢复为出厂默认设置再重新进行设置。关于如何恢复出厂默认设置，请参考第67 页上的将网络设置恢复为出厂默认设置。

![解决无线设置问题及完成后的驱动安装指引](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c90262a0b435ecb70b6787396bd99b6e6159bfcb6fdf86a76b4a48155ffa8e7b.jpg)

无线设置已完成。若要安装打印机驱动程序，请转到第 45 页 ( 适用于 Windows®) 或第 49 页 ( 适用于 Macintosh) 中的步骤 a。

# Windows® 用户 :

# 重要事项

在安装的过程中请勿取消任何屏幕的操作。

a 启动计算机。 ( 必须以管理员身份登录。 )配置前请关闭所有正在运行的应用程序。  
b 将随机光盘插入 CD-ROM 光驱中。将自动显示打开屏幕。选择打印机型号和语言。  
c 出现随机光盘主菜单。点击安装打印机驱动程序。

![安装打印机驱动程序步骤：插入光盘，选择打印机型号和语言，点击安装打印机驱动程序，无线网络用户请点击相应选项。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e4d272a2f9cb3938bf4ad16de9adab4b8f220e96355a8e2baea0d1afa58d8a1a.jpg)

d 点击无线网络用户。

![点击无线网络设置，进入用户帐户控制界面以继续操作。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/36a435af66b1267fdd3d5851120274462ec81686972ca0a4ce158bd08696fbd4.jpg)

![点击无线网络用户后，根据Windows版本不同，在用户帐户控制屏幕选择“允许”或“是”。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/eff4849aa8dfe25bb92aee399464cb1d4537a8f94fda60dff287476556ff9e9c.jpg)

# 注释

当出现用户帐户控制屏幕时：

(Windows Vista®) 点击允许。

(Windows® 7) 点击是。

![用户账户控制提示时选择允许/是，接着仅安装驱动软件并点击下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/5af26fd7a36fa7d4240fa7dbec91475579d50176a1363423cc142a63cda18ff9.jpg)

e 选择仅安装驱动软件，然后点击下一步。

![安装驱动软件选择界面，点击下一步后阅读并同意许可证协议。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c18763a0a2b2fbd281298f1d12ce3688f0be19997ac0df44ec57e16dc2ab144d.jpg)

f 出现许可证协议窗口时，如果您同意该协议，请点击是。

![同意许可证协议后，选择标准安装并点击下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4bccba6b8e6473a3df6d09b6a2ea6f1b9074f97bd7331e69720e6db553a8ce8b.jpg)

# g 选择标准安装，然后点击下一步。

![选择标准安装后，下一步可搜索网络设备或手动输入打印机IP地址/节点名称。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/27be04cda03383ea021c6fb3a8b0fb8057854d2260042c1b21346b3df3cf1b33.jpg)

# h 选择搜索网络中的设备并从已发现的设备列表中选择 (推荐 )，或者输入打印机的 IP 地址或其节点名称，然后点击下一步。

![选择网络中的设备或输入打印机IP地址/节点名称以进行下一步设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c1489a10199b0bbb0c706dd5f4c32566112d51db7cf3d48c8305df6a6c180a80.jpg)

![输入打印机IP地址或节点名称以继续安装过程。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/74570a9af9bdcb34ba46b5adf8ed00722a9afe7a6171a92ad8cc5db6b9fbf848.jpg)

# 注释

通过打印网络配置页，您可以查找到打印机的 IP 地址和节点名称。请参考第 68 页上的打印网络配置页。

# i 选择您的打印机，然后点击下一步。

![选择打印机后，显示网络配置页以查找IP地址和节点名称。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/336b2488ccd060ddd866f8d5a1e58e14a021d0f7e239af6f3d7f00307ea77c2e.jpg)

![选择打印机并点击下一步，若列表未显示可点击刷新，最后点击完成。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a3b2c3f143a0b50913ba0bc79df6dceb4d8ddb460cca8bbd5ab6d199da7525a8.jpg)

# 注释

如果需要较长时间 (1 分钟以上 ) 将打印机显示于列表中，请点击刷新。

# j 点击完成。

![刷新以显示打印机列表，选择后点击完成；若不想添加打印机则跳过。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a97f1d4ea18944c2b903fe2e1f8b0c35fa4609d7870ad07d57bb7e770b10c1b4.jpg)

![设置界面：点击刷新后选择打印机，可选设为默认及启用状态监控器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/204553240133007ae13d77d3dbe9ff2af15d686daa85345ad34ce6fba3afa6c4.jpg)

# 注释

• 如您不想将打印机设置为默认打印机，请勿选中设为默认打印机。  
• 如果您想禁用状态监控器，请勿选中启用状态监控器。

![图片标题：打印机设置选项说明及Mac用户安装指南摘要这张图片主要展示了打印机设置时的两个重要选项（是否设为默认打印机和是否启用状态监控器）的注释，以及对Mac用户在安装过程中的简要指导。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3dafbc12b0f340560b264a2fbab3f94f126fbccbd88d1cc89e02cdc15bf72512.jpg)

# 设置已完成。

# Macintosh 用户：

# 重要事项

在安装的过程中请勿取消任何屏幕的操作。

启动 Macintosh。  
b 将随机光盘插入 CD-ROM 光驱中。双击桌面上的 HL3000 图标，然后双击 Start Here ( 点击此处开始 )图标。选择打印机型号和语言。  
c 出现随机光盘主菜单。点击安装打印机驱动程序。

![安装HL3000打印机驱动程序步骤：从光盘启动，选择打印机型号、语言及无线网络设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/16f7d5be3b7c676a7b43c31c10870c439a9c2474569b0a5c894e8c1b2cfc8a0c.jpg)

d 点击无线网络用户。

![选择仅安装驱动软件并按提示操作，完成后重启Macintosh（适用于Mac OS X 10.3.9）。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9066e842235deac5ec1735889a2668351f460a3ff714e5c30aa1cdd7b183175a.jpg)

e 选择仅安装驱动软件，然后点击下一步。请按照屏幕上的提示执行操作。然后重新启动 Macintosh。 ( 仅适用于 Mac OS X 10.3.9)

![选择仅安装驱动软件并按提示操作，重启Mac后Brother软件将搜索打印机。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/00eb76def1e7b2d12e18f7055f26c8b62b36b9deb81f094fd8d65be8352f69e4.jpg)

f Brother 软件将搜索 Brother 打印机。在此期间将出现以下屏幕。

![Brother软件搜索打印机时的屏幕显示，选择要连接的打印机并点击确定。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9cee4d7525aa13339c522816c5d67118fd7195122fb7ebf793b13eaf4becd968.jpg)

g 选择您想连接的打印机，然后点击确定。

![选择打印机连接界面，展示如何从列表中选取目标打印机并确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e415364a9f19ab768377820e24c11d24496645053dca511877c8bd8df772960f.jpg)

![选择要连接的打印机并点击确定，若有多台同型号则会显示MAC地址以便区分。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9625b12b13cc6c8c61069ca6c7b7bc84f51590ad1e5d849887b28737699c8808.jpg)

# 注释

• 如果网络中存在两台或以上同型号打印机，将在型号名称后面显示 MAC 地址 ( 以太网地址)。您可以向右滚动滚动条以确认 IP 地址。  
• 通过打印网络配置页，您可以查找到打印机的 MAC 地址 ( 以太网地址) 和 IP 地址。请参考第 68页上的打印网络配置页。

# h 出现以下屏幕时，点击好。

![确认IP地址设置完成，显示操作面板界面。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/172e6f129d40c81da7255a544df74104ab941e65ffc14df035a3bffcc55c2650.jpg)

![点击“好”确认设置完成，进入操作面板功能介绍。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3b2d21f8fb76ffb8323cc12fa150bd234f03b1d49b822bec07a2993a41dec246.jpg)

设置已完成。

# 8 操作面板功能

# 概述

本设备的操作面板上有 1 个背亮式液晶显示屏 (LCD)、7 个按钮和 2 个 发光二极管 (LED) 指示灯。液晶显示屏为 16 字符单行显示。

![操作面板介绍：含1个LCD屏、7个按钮及2个LED指示灯，支持更改设置和打印网络配置页等功能。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bc582b6da05f73cd9f776664539dbab3a0eb9e6fb876b56303c4977659dacd7d.jpg)

使用操作面板，您可以进行以下操作：

# 使用操作面板更改打印服务器的设置

请参考第 53 页上的网络菜单。

# 打印网络配置页

请参考第 68 页上的打印网络配置页。

# 将网络设置恢复为出厂默认设置

请参考第67页上的将网络设置恢复为出厂默认设置。

# 网络菜单

在网络环境中使用 Brother 产品前，您需要配置正确的 TCP/IP 设置。

本节将介绍如何使用位于设备前部的操作面板配置网络设置。

通过操作面板上的 Network ( 网络 ) 菜单选项，您可以设置 Brother 设备的网络配置。按任一菜单按钮 (+、-、OK (确定 ) 或 Back (返回 )) 打开主菜单，然后按 + 或 - 键选择 Network (网络 )，找到您想配置的菜单选项。关于此菜单的更多信息，请参考第 138 页上的功能表和出厂默认设置。

请注意，设备随机附带的 BRAdmin Light 实用程序和网络基本管理 ( 网络浏览器 ) 也可用于配置各种网络设置。请参考第 16页上的更改打印服务器设置。

# TCP/IP

此菜单设有 7 个选项：Boot Method ( 引导方式 )、IP Address (IP 地址 )、Subnet Mask ( 子网掩码 )、Gateway ( 网关 )、 IP Boot Tries ( 尝试 IP 启动 )、 APIPA 和 IPv6。

# 引导方式

此选项控制设备获取 IP 地址的方式。默认设置为 Auto ( 自动 )。

![引导方式设置：控制设备获取IP地址的方式，默认为自动，可选静态等模式以避免使用DHCP、BOOTP或RARP。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4a2f0585e860cafc27f41b8cf9d9e68bf525c71d9dd5e043749c8fab42a6d005.jpg)

# 注释

如果您不想通过 DHCP、BOOTP 或 RARP 配置打印服务器，则必须将 Boot Method ( 引导方式 ) 设置为Static ( 静态 )，这样您的打印服务器便会获取一个静态 IP 地址，从而确保打印服务器不会从任何其他系统获取 IP 地址。若要更改引导方式，请使用设备的操作面板、 BRAdmin Light 实用程序或网络基本管理( 网络浏览器 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。

按 OK ( 确定 ) 键。

c 对于 HL-3070CW

( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。

( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。

按 OK ( 确定 ) 键。

d 按 + 或 - 键选择 TCP/IP。

按 OK ( 确定 ) 键。

e 按 + 或 - 键选择 Boot Method ( 引导方式 )。

按 OK ( 确定 ) 键。

f 按 + 或 - 键选择 Auto 1 ( 自动 )、 $\mathtt { S t a t i c } ^ { 2 }$ ( 静态 )、 RARP 3、 BOOTP 4 或 DHCP 5。

按 OK ( 确定 ) 键。

自动模式

在此模式下，设备将扫描网络以搜索 DHCP 服务器。如果搜索到 DHCP 服务器且该服务器已经配置为向设备分配 IP 地址，则设备将使用 DHCP服务器提供的 IP 地址；如果未搜索到 DHCP 服务器，设备将搜索 BOOTP 服务器。如果搜索到 BOOTP 服务器且该服务器已正确配置，则设备将从 BOOTP 服务器获取 IP 地址；如果未搜索到 BOOTP 服务器，设备将搜索 RARP 服务器。如果 RARP 服务器也没有回应，则设备将通过APIPA 协议搜索 IP 地址 ( 请参考第130 页上的使用 APIPA 配置 IP 地址)。初次打开电源后，设备可能需要几分钟时间来扫描网络以搜索服务器。

2 静态模式

在此模式下，您必须手动分配设备的 IP 地址。 IP 地址一旦输入即被锁定。

3 RARP 模式

可以使用逆向地址解析协议 (RARP) 服务在主机上配置 Brother 打印服务器的 IP 地址。关于 BOOTP 的详细信息，请参考 第 130 页上的使用RARP 配置 IP 地址。

4 BOOTP 模式

BOOTP 可以代替 RARP，其优势在于可以配置子网掩码和网关。关于 BOOTP 的详细信息，请参考第 129 页上的使用 BOOTP 配置 IP 地址。

5 DHCP 模式

动态主机配置协议 (DHCP) 是一种自动分配 IP 地址的机制。如果网络 ( 通常为 UNIX、 Windows® 2000/XP、 Windows Vista® 、 Windows® 7 网络 ) 中有 DHCP 服务器，打印服务器将自动从 DHCP 服务器获取 IP 地址，并使用任意与 RFC 1001 和 1002 兼容的动态名称服务来注册名称。

![打印服务器通过DHCP自动获取IP地址并注册名称，或手动设置静态IP以固定地址。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4fd1868b0f1d38122b1cbeaac85d66a5745302ae771a35b8cad1d5f59ea70dd3.jpg)

# 注释

• 如果您不想通过 DHCP、 BOOTP 或 ARP 配置打印服务器，则必须将引导方式设置为静态，这样您的打印服务器便会获取一个静态 IP 地址，从而确保打印服务器不会从任何其他系统获取 IP 地址。若要更改引导方式，使用设备操作面板上的 Network ( 网络 ) 菜单， RAdmin 应用程序或网络基本管理 ( 网络浏览器 )。

• 在小型网络中， DHCP 服务器可以为路由器。

# IP 地址

此栏显示设备当前的 IP 地址。如果您已经将 Boot Method ( 引导方式 ) 设置为 Static ( 静态)，请输入您想分配给设备的 IP 地址 ( 请与网络管理员确认该 IP 地址是否可用 )。如果您选择了 Static ( 静态) 以外的其他方式，设备将尝试使用 DHCP 或 BOOTP 协议获取 IP 地址。设备的默认 IP 地址可能与您网络的 IP 地址编码方式不兼容。 Brother 建议您与网络管理员联系，以获取设备将连接的网络的 IP 地址。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 对于 HL-3070CW( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 TCP/IP。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 IP Address (IP 地址 )。按 OK ( 确定 ) 键。号码的第一组数字将闪烁。  
f 按 + 或 - 键增大或缩小数字。按 OK (确定 ) 键转到下一组数字。  
g 重复上述操作，直至完成 IP 地址设置。  
h 按 OK ( 确定 ) 键确定 IP 地址设置。液晶显示屏的底部将出现一个星号。

# 子网掩码

此栏显示设备当前使用的子网掩码。如果您没有使用 DHCP 或 BOOTP 获取子网掩码，请输入您想配置的子网掩码。请与您的网络管理员确认该子网掩码是否可用。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 对于 HL-3070CW( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 TCP/IP。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Subnet Mask ( 子网掩码 )。按 OK ( 确定 ) 键。号码的第一组数字将闪烁。  
f 按 + 或 - 键增大或缩小数字。按 OK ( 确定 ) 键转到下一组数字。  
g 重复上述操作，直至完成子网掩码地址设置。  
h 按 OK (确定 ) 键确定子网掩码设置。液晶显示屏的底部将出现一个星号。

# 网关

此栏显示设备当前使用的网关或路由器地址。如果您没有使用 DHCP 或 BOOTP 获取网关或路由器地址，请输入您想配置的地址。如果您没有使用网关或路由器，请将此栏留置空白。如有任何疑问，请咨询网络管理员。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。

按 OK ( 确定 ) 键。

c 对于 HL-3070CW

( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。

( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。

按 OK ( 确定 ) 键。

d 按 + 或 - 键选择 TCP/IP。

按 OK ( 确定 ) 键。

e 按 + 或 - 键选择 Gateway ( 网关 )。

按 OK ( 确定 ) 键。号码的第一组数字将闪烁。

f 按 + 或 - 键增大或缩小数字。

按 OK (确定 ) 键转到下一组数字。

g 重复上述操作，直至完成网关地址设置。

h 按 OK ( 确定 ) 键确定网关地址设置。

液晶显示屏的底部将出现一个星号。

# 尝试 IP 启动

此栏显示打印机尝试通过设定的Boot Method ( 引导方式 ) 扫描网络以获取 IP 地址的次数 ( 请参考第 53 页上的引导方式)。默认设置为 3。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 对于 HL-3070CW( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 TCP/IP。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 IP Boot Tries ( 尝试 IP 启动 )。按 OK ( 确定 ) 键。  
f 按 + 或 - 键设置您想尝试获取 IP 地址的次数。按 OK ( 确定 ) 键。

# APIPA

如果将此项设置为 On ( 开 )，当打印服务器无法通过设定的引导方式获取 IP 地址时，打印服务器将在169.254.1.0 至 169.254.254.255 范围内自动指定一个链路本地 IP 地址 ( 请参考第 53 页上的引导方式 )。如果将此项设置为 Off ( 关 )，当打印服务器无法通过设定的引导方式获取 IP 地址时， IP 地址保持不变。APIPA 默认设置为 On ( 开 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 对于 HL-3070CW( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 TCP/IP。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 APIPA。按 OK ( 确定 ) 键。  
f 按 + 或 - 键选择 On ( 开 ) 或 Off ( 关 )。按 OK ( 确定 ) 键。

# IPv6

本设备兼容下一代互联网协议 IPv6。如果您想使用 IPv6 协议，请选择 On (开)。IPv6 的默认设置为 Off (关)。关于 IPv6 协议的详细信息，请浏览以下网站：http://solutions.brother.com/。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 对于 HL-3070CW( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网)。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 TCP/IP。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 IPv6。按 OK ( 确定 ) 键。  
f 按 + 或 - 键选择 On ( 开 ) 或 Off ( 关 )。按 OK ( 确定 ) 键。

![设置IPv6开关及以太网链接模式的步骤说明](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/57d1f481a49692d4f3a5f10ff76023efb70f66f2d89afd6b64143bc8bfbdb658.jpg)

# 注释

如果您将 IPv6 设置为 On ( 开 )，请关闭电源然后再打开，以启用 IPv6 协议。

# 以太网 ( 仅适用于有线网络 )

以太网链接模式。在 Auto (自动 ) 模式下，打印服务器可通过自动协商在 100BASE-TX 全双工 / 半双工或者10BASE-T 全双工 / 半双工模式下运行。

您可以将服务器链接模式固定为 100 BASE-TX 全双工 (100B-FD) / 半双工 (100B-HD) 与 10BASE-T 全双工(10B-FD) / 半双工 (10B-HD)。此更改将在重置打印服务器后生效。默认设置为 Auto ( 自动 )。

![网络模式设置说明及警告，包括100BASE-T与10BASE-T的全/半双工选择，默认自动，错误设置可能导致通信失败。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/1cf8c747e0e4a11ac3b64a42ec6eb5dabaa68b87fba14f65084418ffe6cbead4.jpg)

# 注释

如果设置错误，您可能无法与打印服务器通信。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 Ethernet。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Auto ( 自动 )、 100B-FD、 100B-HD、 10B-FD 或 10B-HD。按 OK ( 确定 ) 键。

# 恢复出厂设置

通过 Factory Reset ( 恢复出厂设置) 功能，您可以将打印服务器恢复为出厂默认设置。关于恢复出厂默认设置的详细信息，请参考第 67 页上的将网络设置恢复为出厂默认设置。

# 设为默认值 ( 适用于 HL-3070CW)

通过 Set to Default ( 设为默认值 ) 功能，您可以将有线网络和无线网络的全部设置恢复为出厂默认值。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c ( 有线网络用户 ) 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。( 无线网络用户 ) 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。

d 按 + 或 - 键选择 Set to Default ( 设为默认值 )。按 OK ( 确定 ) 键。

e 出现 OK? ( 确定？ ) 时，再次按 OK ( 确定 ) 键。

# 启用有线网络 ( 仅适用于 HL-3070CW 有线网络 )

如需使用有线网络连接，请将 Wired Enable ( 启用有线网络 ) 设置为 On ( 开 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 Wired LAN ( 有线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 Wired Enable ( 启用有线网络 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 On ( 开 ) 或 Off ( 关 )。按 OK ( 确定 ) 键。

# 启用无线网络 ( 仅适用于 HL-3070CW 无线网络 )

如需使用无线网络连接，请将 WLAN Enable ( 启用无线网络 ) 设置为 On ( 开 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Enable ( 启用无线网络 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 On ( 开 )。按 OK ( 确定 ) 键。

# SES/WPS 或 AOSS ( 仅适用于 HL-3070CW 无线网络 )

如果您的无线接入点 / 路由器支持 SecureEasySetup、Wi-Fi Protected Setup (PBC 1) 或 AOSS™，则无需使用计算机也可轻松配置您的设备。本 Brother 设备的操作面板上有 SES/WPS/AOSS 菜单。此功能将自动检测您的接入点所要使用的模式 (SecureEasySetup、Wi-Fi Protected Setup 或 AOSS™)。通过按无线接入点 /路由器上的按钮，您可以设置无线网络和安全设置。关于如何进入一键式模式的详细信息，请参考无线接入点 / 路由器附带的指导手册中的相关说明 ( 请参考 第 6 章的3 使用操作面板上的 SES/WPS 或 AOSS 进行的无线配置(适用于HL-3070CW))。

# 有 PIN 密码的 WPS ( 仅适用于 HL-3070CW 无线网络 )

如果您的无线接入点 / 路由器支持 Wi-Fi Protected Setup (PIN 方式 )，则可以轻松进行设备的配置。PIN ( 个人识别码 ) 方式是由 Wi-Fi Alliance 开发的一种连接方式。将 Enrollee ( 本设备 ) 创建的 PIN 输入到注册构件( 管理无线局域网的设备 )，您可以设置无线网络和安全设置。关于如何进入 Wi-Fi Protected Setup 模式的详细信息，请参考无线接入点 / 路由器附带的使用说明书中的相关说明 ( 请参考 第 7 章的使用 Wi-Fi ProtectedSetup 的 PIN 方式的无线配置 ( 适用于 HL-3070CW))。

# 无线网络状态 ( 仅适用于 HL-3070CW 无线网络 )

# 状态

此栏显示当前无线网络状态：Active(11b) ( 可用 (11b))、 Active(11g) ( 可用 (11g))、 Wired LANActive ( 有线网络启用 )、WLAN OFF ( 无线网络关闭 )、Connection Fail ( 连接失败 ) 或 AOSS Active(AOSS 启用 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Status ( 无线网络状态 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Status ( 状态 )。按 OK ( 确定 ) 键。  
f 将显示当前无线网络状态：Active(11b) ( 可用 (11b))、 Active(11g) ( 可用 (11g))、 Wired LANActive ( 有线网络启用 )、 WLAN OFF ( 无线网络关闭 )、 Connection Fail ( 连接失败 ) 或 AOSSActive (AOSS 启用 )。  
g 再次按 OK ( 确定 ) 键。

# 信号

此栏显示当前无线网络状态：Strong ( 强 )、 Medium ( 中 )、 Weak ( 弱 ) 或 None ( 无 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Status ( 无线网络状态 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Signal ( 信号 )。按 OK ( 确定 ) 键。  
f 将显示当前无线网络状态：Strong ( 强 )、 Medium ( 中 )、 Weak ( 弱 ) 或 None ( 无 )。  
g 再次按 OK (确定 ) 键。

# 信道

此栏显示当前无线网络信道。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Status ( 无线网络状态 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Channel ( 信道 )。按 OK ( 确定 ) 键。  
f 将显示当前无线网络信道。  
g 再次按 OK ( 确定 ) 键。

# 速度

此栏显示当前无线网络速度。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Status ( 无线网络状态 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Speed ( 速度 )。按 OK ( 确定 ) 键。  
f 将显示当前无线网络速度。  
再次按 OK ( 确定 ) 键。

# SSID

此栏显示当前无线网络 SSID。显示屏最多可显示 32 个字符的 SSID 名称。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Status ( 无线网络状态 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 SSID。按 OK ( 确定 ) 键。  
f 将显示当前无线网络 SSID。  
再次按 OK ( 确定 ) 键。

# 通信模式

此栏显示当前无线网络通信模式：Ad-hoc 或 Infrastructure ( 基础架构 )。

a 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))。  
b 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
c 按 + 或 - 键选择 WLAN ( 无线局域网 )。按 OK ( 确定 ) 键。  
d 按 + 或 - 键选择 WLAN Status ( 无线网络状态 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Comm. Mode ( 通信模式 )。按 OK ( 确定 ) 键。  
f 将显示当前无线网络通信模式：Ad-hoc 或 Infrastructure ( 基础架构 )。  
g 再次按 OK ( 确定 ) 键。

# 将网络设置恢复为出厂默认设置

您可以将打印服务器恢复为出厂默认设置 ( 重新设置密码和 IP 地址等所有信息 )。

![图片标题：介绍如何通过按键和软件工具将打印服务器恢复至出厂默认设置的方法。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a440f4dafaf044df51fe55f6f7afcc91882429f7d257968963ef974673a0f4c6.jpg)

# 注释

您也可以使用 BRAdmin 应用程序或网络基本管理 ( 网络浏览器 ) 将打印服务器重设为出厂默认设置。如需获取更多信息，请参考第 16 页上的更改打印服务器设置。

确保电源插头已经插上。  
b 启动设备，并等待设备进入准备就绪状态。  
c 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))，使设备脱机。  
d 按 + 或 - 键选择 Network ( 网络 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Factory Reset ( 出厂设置 )。按 OK ( 确定 ) 键。  
f 出现 Restart Printer? ( 重启打印机 ) 时，再次按 OK ( 确定 ) 键。设备将重启。

# 打印网络配置页

![恢复出厂设置并重启打印机后，打印网络配置页，查看默认节点名称。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/56484df42d51ebb3e50225c22208211ed3927c82f8e0b3725ade76e54a8d4157.jpg)

# 注释

节点名称：节点名称显示在网络配置页中。本设备打印服务器的默认节点名称为 "BRNxxxxxxxxxxxx" ( 有线网络 ) 或 "BRWxxxxxxxxxxxx" ( 无线网络 ) ( 适用于 HL-3070CW)。

网络配置页将打印一份报告，其中列有当前的所有网络设置。您可以使用操作面板来打印网络配置页。

确保电源插头已经插上。  
b 启动设备，并等待设备进入准备就绪状态。  
c 按本设备操作面板上的任一菜单按钮 (+、 -、 OK ( 确定 ) 或 Back ( 返回 ))，使设备脱机。  
d 按 + 或 - 键选择 Machine Info. ( 设备信息 )。按 OK ( 确定 ) 键。  
e 按 + 或 - 键选择 Print NetSetting ( 打印机网络设置 )。按 OK ( 确定 ) 键。

![设备信息与网络设置打印步骤及IP地址为0.0.0.0时的处理方法，驱动程序配置向导说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7ae77f2d77b6e3ec15c4edcedb6810a339b2fd86f27f8908370672398ae943c9.jpg)

# 注释

如果网络配置页上的 IP Address (IP 地址 ) 显示为 0.0.0.0，请稍等一分钟后重试。

# 9

# 驱动程序配置向导

# ( 仅适用于 Windows®)

# 概述

驱动程序配置向导软件可方便地安装或自动安装本地连接或与网络连接的打印机。驱动程序配置向导还可以用于创建自我调试型可执行文件，通过在远程计算机上运行该文件，可以实现打印机驱动程序的完全自动化安装。远程计算机无需连接到网络。

# 连接方式

驱动程序配置向导支持三种连接方式。

# 对等

设备连接至网络，但是用户无需通过中央队列即可直接打印到打印机。

![驱动程序配置向导支持对等和网络共享两种连接方式，实现打印机的直接或集中管理打印。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6386901615450d8407b4afbb398545341825a8f862fbf4a2bd8a76118fcd0236.jpg)

1) 客户端计算机  
2) 网络打印机 ( 本设备 )

# 网络共享

设备连接到网络，并使用中央队列管理所有打印作业。

![网络打印机与客户端计算机通过TCP/IP或USB连接，支持网络共享打印及本地打印。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d320a75fc4b5ced8aa040b958a55e2f053afe05bb1452fe76b6d655c9ad51b42.jpg)

1) 客户端计算机  
2) 也称为 “服务器 ” 或 “打印服务器 ”  
3) TCP/IP 或 USB 接口电缆   
4) 打印机 ( 本设备 )

# 本地打印机 (USB 接口电缆 )

用 USB 接口电缆将设备连接到计算机。

![使用USB接口电缆连接打印机与计算机，并通过随机光盘安装驱动程序配置向导。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a1d833d790dd9ab6e1f195b5a2f18b92270ca45bc90b01deea8c6211108887fd.jpg)

1) 客户端计算机  
2) 打印机 ( 本设备 )  
3) USB 接口电缆

# 如何安装驱动程序配置向导软件

a 将随机光盘插入 CD-ROM 光驱中。出现型号名称屏幕时，选择本设备。出现语言屏幕时，选择所需语言。  
b 出现随机光盘主菜单。点击安装其他驱动程序或实用程序。  
c 选择驱动程序配置向导安装程序。

![光盘插入后选择设备与语言，进入主菜单安装驱动程序，并根据系统提示完成用户控制和许可协议步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8d9a7d1c2ee9d5c99f286f7768e1eaacd6bd5395c6f9692453d2134fa385e77f.jpg)

# 注释

当出现用户帐户控制屏幕时：

(Windows Vista®) 点击允许。

(Windows® 7) 点击是。

d 出现“ 欢迎 ” 信息时，点击下一步。  
e 仔细阅读许可证协议，然后遵循屏幕上的提示执行操作。  
f 点击完成。至此，驱动程序配置向导软件已经安装完成。

# 使用驱动程序配置向导软件

a 首次运行配置精灵时会出现欢迎屏幕，此时请点击下一步。  
b 选择打印机，然后点击下一步。  
c 选择目标打印机的连接类型。   
d 选择所需选项，并遵循屏幕上的提示执行操作。如果您选择 Brother 对等网络打印机，将出现以下屏幕 :

![设置打印机连接类型及IP地址配置步骤说明](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/584cdd42bcddec0c182302ba82dd84fad0c1969ef45e52608754b83e263c1738.jpg)

#  设置 IP 地址

如果设备没有 IP 地址，您可以使用精灵通过选择列表中的设备并选择 “ 配置 IP” 选项来更改 IP 地址。出现一个对话框，提示您指定 IP 地址、子网掩码和网关地址等信息。

![设置设备IP地址及选择安装打印机驱动程序的步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/13311d25caa19bec6c935b6efea1a233a348170ccf2b791363838602571610d0.jpg)

# e 选择您想安装的设备。

 计算机上已安装您想使用的打印机驱动程序时：  
选中目前已安装的驱动程序的复选框，选择您想安装的打印机，然后点击下一步。  
 计算机上未安装您想使用的打印机驱动程序时：

1 点击从磁盘安装 ...。  
2 选择您想使用的操作系统 (OS)，然后点击确定。  
3 点击浏览并选择随机光盘或网络共享中适用的打印机驱动程序，然后点击打开。

4 例如，选择 "X:\install\your language\PCL\32 1" 文件夹 (X 为光驱的盘符 )，然后点击确定。

1 对于 32 位 OS 用户，此处为 32 文件夹；对于 64 位 OS 用户，此处为 64 文件夹。

![选择对应操作系统位数的文件夹安装驱动，并确认设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/76bfb294f73e07061d4278abd7ec0957a7f46fb8785b98763e074f75a32dc8c2.jpg)

f 选择正确的驱动程序后点击下一步。  
g 将出现总结屏幕。确认驱动程序的设置。

![选择并确认驱动程序后，可使用向导创建自我调试型.EXE文件以便分享。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a2ae4327d53388b95d7bd5a7434f722fde16deb75654f988fc51632d4047ba65.jpg)

#  创建可执行文件

驱动程序配置向导软件还可用于创建自我调试型 .EXE 文件。可以将这些自我调试型 .EXE 文件保存到网络中、复制到光盘或 USB 内存中或者通过电子邮件发送给其他用户。驱动程序与其设置一旦运行将自动安装，无需用户干涉。

• 将驱动程序文件复制到计算机中并为其他用户创建一个安装程序。

如果您想将驱动程序安装到计算机上并创建一个自我调试型可执行文件，且要求此计算机与您的计算机使用相同的操作系统，请选择此选项。

• 仅为其他用户创建一个驱动程序。

如果计算机上已安装驱动程序并且您想创建一个自我调试型可执行文件，同时又不想在计算机上再次安装驱动程序，请选择此选项。

![选择创建驱动程序或自我调试型可执行文件，以便其他用户访问同一打印机队列。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/0905a69382c6ad07947e027147d205a39172bc20864f87e09579cd3eb1bcf94a.jpg)

# 注释

• 如果您所在的网络以 “ 队列 ” 为基础，并且您想为其他用户创建一个可执行文件以使他们能够访问可执行文件中指定的同一打印机队列，则当驱动程序安装到远程计算机上时，默认设置为 LPT1 打印。  
• 如果您在步骤 e 中选中目前已安装的驱动程序复选框，则您可以通过点击自定义 ... 更改纸张尺寸等打印机驱动程序的默认设置。

h 点击完成。驱动程序已自动安装到计算机上。

# 10 网络基本管理

# 概述

标准网络浏览器可用于管理使用 HTTP (超文本传输协议 ) 的设备。可以使用网络浏览器从您的网络设备上：

 查看设备状态信息  
 更改 TCP/IP 信息等网络设置  
 查看设备和打印服务器的软件版本信息  
 更改网络和设备配置详细信息

![通过网络浏览器访问设备，查看状态、更改设置及配置信息；建议使用IE 6.0+或Firefox 1.0+。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/52d56f285232ddd114af53ce512b2fa35244d1021eb1335e61578738c7ce00fa.jpg)

# 注释

Brother 建议 Windows® 用户使用 Microsoft® Internet Explorer® 6.0 ( 或更高版本 ) 或 Firefox 1.0 ( 或更高版本 )，Macintosh 用户使用 Safari 1.3 ( 或更高版本 )。无论使用何种浏览器，请确保始终启用 JavaScript和 Cookies。如果使用其他网络浏览器，请确保与 HTTP 1.0 和 HTTP 1.1 兼容。

必须使用网络中的 TCP/IP 协议，且已输入打印服务器和计算机的有效 IP 地址。

![图片标题：配置说明，涉及脚本、Cookies兼容性要求及TCP/IP协议使用，指引IP地址设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8652451945792c5ec62eafe778f3495b4692c082f00c8b428e83b07bf43cf520.jpg)

# 注释

• 关于如何配置设备 IP 地址，请参考第 13 页上的设置 IP 地址和子网掩码。  
• 可以使用大多数计算平台上的网络浏览器，例如， Macintosh 和 UNIX 用户也可以连接至设备并对其进行管理。  
• 也可以使用 BRAdmin 应用程序管理设备及其网络配置。  
• 本打印服务器支持 HTTPS，以使用 SSL 进行安全管理。请参考第 93页上的安全管理网络打印机。

# 如何使用网络基本管理 ( 网络浏览器 ) 配置打印服务器设置

可通过标准网络浏览器更改使用 HTTP (超文本传输协议 ) 的打印服务器设置。

![使用网络浏览器通过输入打印机IP地址访问并配置打印服务器设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3c3d5665350aa20a7bf5a73af55e458a16f845d2c3a68761b519970ff1e76221.jpg)

# 注释

若要使用网络浏览器，您需要知道打印服务器的 IP 地址或节点名称。

打开您的网络浏览器。  
b 在您的浏览器中输入 “http://printer's IP address/” (“printer's IP address” 为打印机的IP 地址 )。

 例如：

```txt
http://192.168.1.2/ 
```

![示例展示了如何通过输入打印机的IP地址（如`http://192.168.1.2/`）或DNS名称访问打印服务器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b30aa4f367b177df5cb17cba48b026c58ecc671ede2700fa972ca1ea4b59512d.jpg)

# 注释

• 如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统 (DNS)，您也可以输入打印服务器的DNS 名称。  
• 对于 Windows® 用户，因为打印服务器支持 TCP/IP 和 NetBIOS 名称，所以您也可以输入打印服务器的NetBIOS 名称。 NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68页上的打印网络配置页。NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为 "BRNxxxxxxxxxxxx"( 有线网络 ) 或 "BRWxxxxxxxxxxxx" ( 无线网络 )。  
• Macintosh 用户也可以通过点击 “ 状态监控器” 屏幕上的设备图标，方便地访问网络基本管理系统。如需获取更多信息，请参考随机光盘上的使用说明书。

c 点击网络配置。  
d 输入用户名和密码。默认用户名为 "admin"，默认密码为 "access"。  
e 点击确定。  
f 此时可以更改打印服务器设置。

![网络配置步骤：点击配置，输入默认用户名"admin"和密码"access"，更改打印服务器设置并提交。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7e9dea0ed8db419f49938a6eb0f01f5bfe9660057db2955b15204a4b6538238b.jpg)

# 注释

如果您已经更改了协议设置，请点击提交，然后重启打印机以启用配置。

# 11 在 Windows® 操作系统下进行网络打印：基本 TCP/IP 对等打印

# 概述

若要将设备连接至网络，需执行快速安装指南中的相关步骤。Brother 建议您使用随机光盘上的 Brother 安装程序。使用此应用程序，可简便地将设备连接至您的网络，并安装完成网络设备配置所需的网络软件和打印机驱动程序。屏幕提示将指导您如何进行配置，直至您可以使用 Brother 网络设备。

如果您使用 Windows® 操作系统，并且不想通过 Brother 安装程序配置设备，则可以使用对等环境中的TCP/IP 协议。请遵循本章的说明执行操作。本章阐述如何安装使用网络设备所需的网络软件和打印机驱动程序。

![使用TCP/IP协议在对等环境中配置网络设备及打印机驱动程序，需预先设置IP地址并确保主机与设备同子网。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/f010383b867fa60fc6d272590cef45f54ccd2935f260d32eff584543d52093f1.jpg)

# 注释

• 在进行本章操作之前，您必须配置设备的 IP 地址。如需配置 IP 地址，请参考第2 章。  
• 验证主机和设备是否在同一子网中，或者路由器是否正确配置以便在两设备之间传输数据。  
• 若要连接至网络打印队列或共享 ( 仅打印 )，请参考第 134 页上的使用网络打印队列或共享时的安装中的安装详情。  
• Brother 打印服务器的默认密码为 "access"。

# 配置标准 TCP/IP 端口

# 尚未安装打印机驱动程序

# Windows Vista® 、 Windows® 7 和 Windows Server® 2008

a (Windows Vista®) 点击 按钮、控制面板、硬件和声音，然后点击打印机。

(Windows® 7) 点击 按钮，设备和打印机。

(Windows Server® 2008) 点击开始按钮、控制面板、硬件和声音，然后点击打印机。

b 点击添加打印机。  
c 选择添加本地打印机。  
d 此时必须选择正确的网络打印端口。选择创建新端口，然后从下拉窗口中选择 Standard TCP/IP Port( 标准 TCP/IP 端口 )，然后点击下一步。  
e 从设备类型的下拉窗口中选择 TCP/IP 设备。输入 IP 地址或您想配置的节点名称。向导将自动为您输入相关的端口名称信息，然后点击下一步。  
f 此时 Windows Vista® 、Windows® 7 和 Windows Server® 2008 将连接您指定的打印机。如果未指定正确的 IP 地址或名称，将出现错误对话框。  
g 如果已配置好端口，您必须指定要使用的打印机驱动程序。从支持的打印机列表中选择合适的驱动程序。如果使用设备随机光盘上的驱动程序，请选择从磁盘安装选项以浏览随机光盘中的内容。  
h 例如，选择 "X:\install\your language\PCL\32 1" 文件夹 (X 为光驱的盘符 )，然后点击打开。

i 指定打印机名称，然后点击下一步。

![安装打印机驱动：选择光盘中对应文件夹，指定打印机名称，并根据系统提示完成安装。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6ceb3a872f0f59a3d613cecaaaf3f200aa784495a0ab6372f454067a2ebd7d65.jpg)

# 注释

• 当出现用户帐户控制屏幕时：

(Windows Vista®) 点击继续。

(Windows® 7) 点击是。

• 如果您安装的打印机驱动程序没有数字证书，将出现警告信息。点击始终安装此驱动程序软件以继续安装。

j 待向导完成安装后，点击完成。

# Windows® 2000/XP 和 Windows Server® 2003

Windows® XP 和 Windows Server® 2003 用户：点击开始按钮，然后选择打印机和传真。  
Windows® 2000 用户：  
点击开始按钮，选择设置，然后选择打印机。

b Windows® XP 和 Windows Server® 2003 用户：点击添加打印机以启动添加打印机向导。

Windows® 2000 用户：

双击添加打印机图标以启动添加打印机向导。

c 当出现欢迎使用添加打印机向导屏幕时，点击下一步。

d 选择连接到此计算机的本地打印机，请勿选中自动检测并安装即插即用打印机选项，然后点击下一步。

e 此时必须选择正确的网络打印端口。选择创建新端口，然后从下拉窗口中选择 Standard TCP/IP Port( 标准 TCP/IP 端口 )，然后点击下一步。

f 将显示添加标准 TCP/IP 打印机端口向导。点击下一步。

g 输入 IP 地址或您想配置的节点名称。向导将自动为您输入相关的端口名称信息，然后点击下一步。

h 此时 Windows® 2000/XP 和 Windows Server® 2003 将连接您指定的设备。如果未指定正确的 IP 地址或名称，将出现错误对话框。

i 待向导完成安装后，点击完成。

j 如果已配置好端口，您必须指定要使用的打印机驱动程序。从支持的打印机列表中选择合适的驱动程序。如果使用设备随机光盘中的驱动程序，请选择从磁盘安装选项以浏览随机光盘中的内容。

k 例如，选择 "X:\install\your language\PCL\32 1" 文件夹 (X 为光驱的盘符 )，然后点击打开。

1 对于 32 位 OS 用户，此处为 32 文件夹；对于 64 位 OS 用户，此处为 64 文件夹。

l 指定打印机名称，然后点击下一步。

m 待向导完成安装后，点击完成。

# 已安装打印机驱动程序

如果您已安装打印机驱动程序并需要对其进行配置以进行网络打印，请执行以下步骤：

a Windows Vista® 、 Windows® 7 和 Windows Server® 2008 用户：

(Windows Vista®) 点击 按钮、控制面板、硬件和声音，然后点击打印机。

(Windows® 7) 点击 按钮，设备和打印机。

(Windows Server® 2008) 点击开始按钮、控制面板、硬件和声音，然后点击打印机。

Windows® XP 和 Windows Server® 2003 用户：

点击开始按钮，然后选择打印机和传真窗口。

Windows® 2000 用户：

点击开始按钮，并选择设置，然后选择打印机。

b 右击要配置的打印机驱动程序，然后选择属性。  
c 点击端口选项卡，然后点击添加端口。  
d 选择要使用的端口。通常选择 Standard TCP/IP Port ( 标准 TCP/IP 端口 )。然后点击新端口 ... 按钮。  
e 将启动添加标准 TCP/IP 打印机端口向导。点击下一步。  
f 输入网络打印机的 IP 地址，然后点击下一步。  
点击完成。  
h 关闭打印机端口和属性对话框。

# 其他信息来源

关于如何配置设备的 IP 地址，请参考第 10 页上的配置网络设备和第 18 页上的配置无线网络设备 ( 适用于HL-3070CW)。

# 12 在 Windows® 操作系统下进行网络打印

# 概述

Windows® 2000/XP、 Windows Vista®、 Windows® 7 和 Windows Server® 2003/2008 用户可以通过使用内置标准网络打印协议 (IPP) 软件的 TCP/IP 进行打印。

![介绍如何通过TCP/IP使用IPP协议在特定Windows系统上进行网络打印，并提醒需预先配置打印机IP地址及确保与主机同子网或正确路由配置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/86b0f8515d9e1fb429d65c20a40dcd54bd45cc3ae3892adb25551e0c46136108.jpg)

# 注释

• 在进行本章操作之前，您必须配置打印机的 IP 地址。如需配置 IP 地址，首先请参考第2 章。  
• 验证主机和设备是否在同一子网中，或者路由器是否正确配置以便在两设备之间传输数据。  
• Brother 打印服务器的默认密码为 "access"。  
• 本打印服务器同时支持 IPPS 打印，请参考第 100页上的使用 IPPS 安全打印文档。

# 在 Windows® 操作系统下进行的 IPP 打印

如果您想使用 Windows® 2000/XP、Windows Vista® 、Windows® 7 和 Windows Server® 2003/2008 操作系统下的 IPP 打印功能，请执行以下操作。

操作步骤可能会因操作系统的不同而有所不同。

# Windows Vista® 、 Windows® 7 和 Windows Server® 2008

a (Windows Vista®) 点击 按钮、控制面板、硬件和声音，然后点击打印机。

(Windows® 7) 点击 按钮，设备和打印机。

(Windows Server® 2008) 点击开始按钮、控制面板、硬件和声音，然后点击打印机。

b 点击添加打印机。  
c 选择添加网络、无线或 Bluetooth 打印机。  
d 点击我需要的打印机不在列表中。  
e 选择按名称选择共享打印机，然后在 URL 栏内输入以下内容：

http://printer's IP address:631/ipp ("printer's IP address" 为打印机的 IP 地址或节点名称 )。

![在URL栏输入打印机IP地址或DNS名称访问打印服务器配置页面。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3892ac959d8e7921f925422d4e9eb4f09d32828006c8bd2be92fd5324124dd9b.jpg)

# 注释

如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统 (DNS)，您也可以输入打印服务器的 DNS名称。因为打印服务器支持 TCP/IP 和 NetBIOS 名称，所以您也可以输入打印服务器的 NetBIOS 名称。NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68 页上的打印网络配置页。NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为 "BRNxxxxxxxxxxxx" ( 有线网络 ) 或"BRWxxxxxxxxxxxx" ( 无线网络 )。

f 当您点击下一步时， Windows Vista® 、 Windows® 7 和 Windows Server® 2008 将与您指定的 URL 连接。

 如果已安装打印机驱动程序：

在添加打印机中将出现打印机选择屏幕。点击确定。

如果计算机上已安装正确的打印机驱动程序， Windows Vista® 、 Windows® 7 和 Windows Server®2008 将自动应用此驱动程序。在此情况下，计算机将询问您是否希望将驱动程序设置为默认驱动程序，此后驱动程序安装向导才会完成。此时打印准备就绪。

请转到步骤 k。

 如果尚未安装打印机驱动程序：

IPP 打印协议的一个优点是当您与打印机进行通信时，它可以创建打印机的型号名称。通信成功后将自动显示打印机的型号名称。这就意味着您无需通知 Windows Vista® 、 Windows® 7 或 WindowsServer® 2008 将要使用的打印机驱动程序的类型。

请转到步骤 g。

g 如果您的打印机不在支持的打印机列表中，点击从磁盘安装。计算机将提示您插入驱动盘。  
h 点击浏览，并选择随机光盘或网络共享中适用的 Brother 打印机驱动程序，然后点击打开。例如，选择 "X:\install\your language\PCL\32 1" 文件夹 (X 为光驱的盘符 )，然后点击打开。

i 点击确定。  
j 指定打印机的型号名称，然后点击确定。

![选择安装路径，确认打印机型号，处理用户帐户控制及驱动警告，完成打印机添加。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/927382d7d5483730624f75e0e343cc72c019060947b931396508bcf982f027ec.jpg)

# 注释

• 出现用户帐户控制屏幕时，点击继续或是。  
• 如果您安装的打印机驱动程序没有数字证书，将出现警告信息。点击始终安装此驱动程序软件以继续安装。完成添加打印机向导。

k 在添加打印机中将出现打印机名称屏幕。如果您想将此打印机作为默认打印机使用，请选中设置为默认打印机复选框，然后点击下一步。  
l 若要测试打印机连接，点击打印测试页，然后点击完成，此时打印机配置完成，打印准备就绪。

# Windows® 2000/XP 和 Windows Server® 2003

Windows® XP 和 Windows Server® 2003 用户：点击开始按钮，然后选择打印机和传真。

Windows® 2000 用户：

点击开始按钮，并选择设置，然后选择打印机。

b Windows® XP 和 Windows Server® 2003 用户：点击添加打印机以启动添加打印机向导。

Windows® 2000 用户：

双击添加打印机图标以启动添加打印机向导。

c 当出现欢迎使用添加打印机向导屏幕时，点击下一步。

d 选择网络打印机。

Windows® XP 和 Windows Server® 2003 用户：

选择网络打印机或连接到其他计算机的打印机。

Windows® 2000 用户：

选择网络打印机。

e 点击下一步。

f Windows® XP 和 Windows Server® 2003 用户：

选择连接到 Internet、家庭或办公网络上的打印机，然后在 URL 栏中输入以下内容：

http://printer's IP address:631/ipp

("printer's IP address" 为打印机的 IP 地址或节点名称 )。

Windows® 2000 用户：

选择连接到 Internet 或内部网上的打印机，然后在 URL 栏中输入以下内容：

http://printer's IP address:631/ipp

("printer's IP address" 为打印机的 IP 地址或节点名称。 )

![在浏览器URL栏输入打印机IP地址和端口631/ipp访问，或使用DNS名称访问打印服务器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b9cdd3b8cf4e7c611dfef8043a0a9d9f9c48085f02abdb2eb8d4fa4021e7f337.jpg)

# 注释

如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统 (DNS)，您也可以输入打印服务器的 DNS名称。因为打印服务器支持 TCP/IP 和 NetBIOS 名称，所以您也可以输入打印服务器的 NetBIOS 名称。NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68 页上的打印网络配置页。NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为 "BRNxxxxxxxxxxxx" ( 有线网络 ) 或"BRWxxxxxxxxxxxx" ( 无线网络 )。

g 当您点击下一步时， Windows® 2000/XP 和 Windows Server® 2003 将与您指定的 URL 连接。

 如果已安装打印机驱动程序：

如果计算机上已安装正确的打印机驱动程序，Windows® 2000/XP 和 Windows Server® 2003 将自动应用此驱动程序。在此情况下，计算机将询问您是否希望将驱动程序设置为默认驱动程序，此后驱动程序安装向导才会完成。此时打印准备就绪。

请转到步骤 l。

 如果尚未安装打印机驱动程序：

IPP 打印协议的一个优点是当您与打印机进行通信时，它可以创建打印机的型号名称。通信成功后将自动显示打印机的型号名称。这就意味着您无需通知 Windows® 2000 将要使用的打印机驱动程序的类型。

请转到步骤 h。

h 自动启动驱动程序安装。

![自动检测并显示打印机型号，启动驱动程序安装，无数字证书时选择继续安装。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/f7b888ad5d5255ce13e65b04fbedb28095633747371c4b134ae8a48594bd12d9.jpg)

# 注释

如果您安装的打印机驱动程序没有数字证书，将出现警告信息。点击始终安装此驱动程序软件 1 以继续安装程序。

1 Windows® 2000 的用户为是。

i 出现插入磁盘屏幕时，点击确定。  
j 点击浏览并选择随机光盘或网络共享中适用的 Brother 打印机驱动程序，然后点击打开。

例如：选择 "X:\install\your language\PCL\32 1" 文件夹 (X 为光驱的盘符 )，然后点击打开。

1 对于 32 位 OS 用户，此处为 32 文件夹；对于 64 位 OS 用户，此处为 64 文件夹。

点击确定。  
l 如果将此打印机作为默认打印机使用，请选中是，然后点击下一步。  
m 点击完成，打印机配置完成，打印准备就绪。若要测试打印机连接，请打印测试页。

# 指定一个不同的 URL

敬请注意，您可以根据需要在 URL 栏中输入以下地址：

```html
http://printer's IP address:631/ipp 
```

这是默认的 URL， Brother 建议您使用此 URL。

```txt
http://printer's IP address:631/ipp/port1 
```

此 URL 与 HP Jetdirect 兼容。

```txt
http://printer's IP address:631/ 
```

![HP Jetdirect兼容URL说明：使用`http://打印机IP地址:631/`访问，忘记详情时仅输入基础URL也可。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b96f4e261bbfe9e458c8d765f83aa9ee760efe006d845d4929c2d1ac7e4fad28.jpg)

# 注释

如果忘记了 URL 的详细内容，您只需输入上述文本 (http://printer's IP address/)，打印机仍将接收和处理数据。

"printer's IP address" 为打印机的 IP 地址或节点名称。

 例如：

```txt
http://192.168.1.2/ 
```

```html
http://BRN123456765432/ 
```

# 其他信息来源

关于如何配置打印机的 IP 地址，请参考第 2 章的配置网络设备。

# 13

# 在 Macintosh 操作系统下使用 BR-Script 3驱动程序进行网络打印 ( 适用于 HL-3070CW)13

# 概述

本章阐述如何在网络中配置 BR-Script 3 (PostScript® 3™ 仿真语言 ) 打印机驱动程序。

# 如何选择打印机驱动程序 (TCP/IP)

# Mac OS X 10.3.9 至 10.4.x 用户

打开 Macintosh。  
b 在 Go ( 开始 ) 菜单中选择 Applications ( 应用程序 )。  
c 打开 Utilities ( 实用程序 ) 文件夹。  
d 双击 Printer Setup Utility ( 打印机设置实用程序 ) 图标。  
e 点击 Add ( 添加 )。  
f (Mac OS X 10.3.9) 选择 IP 打印。(Mac OS X 10.4.x) 选择 IP 打印机。

(Mac OS X 10.3.9)   
![Mac OS X系统中选择IP打印机的步骤说明，针对10.3.9和10.4.x版本。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/da84bc8b779bf4f0b57816d4eb0773cffc50a0e5d9d1e58f7928aa0ff573d969.jpg)

(Mac OS X 10.4.x)   
![在Mac OS X 10.3.9和10.4.x系统中，于打印机设置界面输入打印机IP地址的步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/33adb8d76306936ec87113eaf687621621ac2daae6c81abd03f33ea2607cf3c5.jpg)

g (Mac OS X 10.3.9) 在打印机地址栏中输入打印机的 IP 地址。(Mac OS X 10.4.x) 在地址栏中输入打印机的 IP 地址。

(Mac OS X 10.3.9)   
![在Mac OS X 10.3.9和10.4.x系统中，于地址栏输入打印机IP地址以添加网络打印机。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/fe4d50aedeaa91049acf73428ea4bd7c9bc4c92c5c775d681c69007675cfea1b.jpg)

(Mac OS X 10.4.x)   
![Mac OS X 10.4.x系统下网络配置页面示意图，展示网络设置选项。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/35c4baac7bade73e2395888ba581113b3713cae4dba01e2ed0a12c84ce9a541d.jpg)

![网络配置页示例，展示如何在Mac OS X 10.4.x系统中查看和设置IP地址及队列名称。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a2ea38cfc97402215a970cd422abde5f01c45f96215bbbf8a1b5c1190d5a0b0e.jpg)

# 注释

• 可在网络配置页中确认 IP 地址。关于打印网络配置页，请参考第 68页上的打印网络配置页。  
• 对于 Macintosh 用户，指定队列名称 ( 队列 ) 时，请使用 PostScript® 服务 "BRNxxxxxxxxxxxx\_AT"。"xxxxxxxxxxxx" 为本设备的 MAC 地址 ( 以太网地址 )。

h 在打印机型号 ( 打印使用 ) 弹出菜单中选择您的设备型号。例如，选择 Brother HL-3070CW BR-Script3。

(Mac OS X 10.3.9)   
![选择打印机型号设置示例：Brother HL-3070CW BR-Script3 (适用于Mac OS X 10.3.9及10.4.x)](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/2c823d32e30505a0b0b1265f384814e97e7b67d425f8d14c7b8f404bb8a2f8c4.jpg)

(Mac OS X 10.4.x)   
![Mac OS X 10.4.x系统下，通过点击添加选择打印机，并为10.5.x-10.6.x用户提供初步指导。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/aca1fa04954f5d88a6711dabe1c88a9f3a04f45bbf32f713454c789f8929a982.jpg)

i 点击添加，从打印机列表中选择可使用的打印机。此时，打印机准备就绪。

# Mac OS X 10.5.x - 10.6.x 用户

打开 Macintosh。  
b 在 Apple 菜单中选择 System Preferences ( 系统偏好设置 )。  
c 选择 Print & Fax ( 打印和传真 ) 。  
d 点击位于 Printers ( 打印机 ) 选项下方的 +。  
e 选择 IP。

![通过系统偏好设置中的打印与传真选项添加IP打印机，并选择LPD协议及输入打印机地址。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6a58faf3abf098d1b63b9b5243cc549721c39f273afde06f1d2bde0287cdb321.jpg)

f 在协议列表中选择行式打印机监控程序 - LPD。  
g 在地址栏中输入打印机的 TCP/IP 地址或 DNS 名称。

![在协议列表中选择LPD，并输入打印机的TCP/IP地址或DNS名称。Mac用户需使用特定PostScript服务指定队列。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3918c4bbc5dc188dab7d95ad1bb232d07319b50446abcdc61c7e4814821b80bd.jpg)

# 注释

对于 Macintosh 用户，指定队列时，请使用 PostScript® 服务 "BRNxxxxxxxxxxxx\_AT"。"xxxxxxxxxxxx" 为本设备的 MAC 地址 ( 以太网地址 )。

![Mac用户需使用含设备MAC地址的PostScript服务，并在打印设置中选择正确的设备型号。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9237cd7acd437918fb2b719749616281c74011a813ca1a36ee951f44bc1300b8.jpg)

h 在打印使用弹出菜单中选择您的设备型号。例如，选择 Brother HL-3070CW BR-Script3。

![选择设备型号并添加打印机，确保其在网络中准备就绪。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c7b1cd0b6e9795bc23cfa12b3a4e40315c3fddb33e1c515906c3e4c463513afb.jpg)

i 点击添加，打印机栏中将显示您添加的打印机。此时，打印机准备就绪。

# 14 安全性能

# 概述

当今，网络及网络上传输的数据存在很多安全隐患。 Brother 产品采用了当前可用的最新网络安全与加密协议。这些网络功能可以应用于网络安全总计划中，有助于保护数据并防止未经授权用户访问该设备。本章阐述本款产品所支持的多种安全协议和如何对其进行配置。

# 安全术语

 CA ( 证书授权中心 )

CA 认证中心是颁发数字证书 ( 尤其是 X.509 证书 ) 并证明证书中数据项目间具有约束力的一个机构。

 CSR ( 证书签订请求 )

CSR 是申请人向 CA 认证中心申请签发证书的一个请求。 CSR 包含申请人验证资料，申请人公共键及申请人数字签名。

 证书

证书是将公共键和身份结合在一起的一种信息。证书可以用于验证公共键是否属于个人。格式由 x.509 标准进行定义。

 数字签名

数字签名是使用加密法则计算出的一个值，并且可以添加在数据对象上，这样数据接收者可以通过签名来验证数据来源及其真实性。

 公共键加密系统

公共键加密系统是加密系统的一个现代分支，它使用一对键 ( 公共键和机密键 ) 及其不同组件来完成不同步骤的法则计算。

 共享键加密系统

共享键加密系统是加密系统的一个分支，它具备使用同一键进行的两个不同计算步骤 ( 如加密和解密) 的法则步骤。

# 安全协议

Brother 打印服务器支持以下安全协议。

![共享键加密系统介绍及Brother打印服务器支持的安全协议概览，包括SSL/TLS等。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8007bc52ab34fc9d3dc488515b60cd0e3e5f583899593b74a36b238b1915c56f.jpg)

# 注释

关于如何配置协议设置，请参考第 76页上的如何使用网络基本管理 ( 网络浏览器) 配置打印服务器设置。

# SSL ( 安全套接层 ) / TLS ( 传输层安全 )

这些安全通信协议可以加密数据以防止安全隐患。

# 网络服务器 (HTTPS)

超文本传输协议 (HTTP) 使用 SSL 的网络协议。

# IPPS

网络打印协议 (IPP 版本 1.0) 使用 SSL 的打印协议。

# SNMPv3

简单网络管理协议版本 3 (SNMPv3) 提供了用户验证和数据加密以便安全管理网络设备。

# 电子邮件通知的安全方法

Brother 打印服务器支持以下电子邮件通知的安全方法。

![SNMPv3提供安全网络管理，Brother打印服务器支持的电子邮件通知安全方法及配置指南。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/dd88f2c77f4b6c03bf00020a034489172e78df1d0cd2b685049f13fd6ba6776a.jpg)

# 注释

关于如何配置安全方法设置，请参考第 76 页上的如何使用网络基本管理 ( 网络浏览器) 配置打印服务器设置。

# POP 优先于 SMTP (PbS)

从客户端发送电子邮件的用户验证方法。发送电子邮件之前，通过访问 POP3 服务器，客户端可以使用SMTP 服务器。

# SMTP-AUTH (SMTP 验证 )

SMTP-AUTH 扩展了 SMTP (网络电子邮件发送协议 )，使其具备了可以确定发件人真实身份的验证方法。

# APOP ( 带验证的邮局协议 )

APOP 扩展了 POP3 (网络接收协议 )，使其具备了在客户端接收电子邮件时进行加密的验证方法。

# 配置协议设置

使用网络基本管理 ( 网络浏览器 ) 可以启用或禁用各种协议和安全方法。

![APOP扩展了POP3，增加加密验证；通过网络浏览器管理协议设置；建议使用特定版本的IE或Firefox。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bf5ab113de25fe09464d57c58031b1a6ddad1b3dd7dab785655a3e8399356667.jpg)

# 注释

Brother 建议 Windows® 用户使用 Microsoft® Internet Explorer® 6.0 ( 或更高版本 ) 或 Firefox 1.0 ( 或更高版本 )，Macintosh 用户使用 Safari 1.3 ( 或更高版本 )。无论使用何种浏览器，请确保始终启用 JavaScript和 Cookies。如果使用其他网络浏览器，请确保其与 HTTP 1.0 和 HTTP 1.1 兼容。若要使用网络浏览器，您需要知道打印服务器的 IP 地址。

打开您的网络浏览器。  
b 在您的浏览器中输入 http://printer's IP address/ (“printer's IP address” 为打印机的 IP地址 )。

 例如：

http://192.168.1.2/

![通过输入打印机IP地址访问网络设置，也可使用DNS名称，支持TCP/IP协议。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/0af01e026916654cf92b356c420b8a7e4906ec665b61510c3fd6397638e33aac.jpg)

# 注释

• 如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统，您也可以输入打印服务器的 DNS 名称。  
• 对于 Windows® 用户，因为打印服务器支持 TCP/IP 和 NetBIOS 名称，所以您也可以输入打印服务器的NetBIOS 名称。 NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68页上的打印网络配置页。NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为 "BRNxxxxxxxxxxxx"( 有线网络 ) 或 "BRWxxxxxxxxxxxx" ( 无线网络 )。

c 点击网络配置。  
d 输入用户名和密码。默认用户名为 “admin”，默认密码为 “access”。  
e 点击确定。  
f 点击配置协议。此时您可以配置协议设置。

![网络配置步骤：点击网络配置，输入默认用户名和密码，点击确定后配置协议设置。更改设置需重启打印机。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d73be2eae8d54245e7b13fde7a2f6399f67ccd1d808fe3abbede96399f1b9f35.jpg)

# 注释

如果您要更改协议设置，点击提交后，重启打印机，以激活配置。

# 安全管理网络打印机

若要安全管理网络打印机，您必须通过安全协议来使用管理实用程序。

# 使用网络基本管理 ( 网络浏览器 ) 的安全管理

Brother 建议您使用 HTTPS 和 SNMPv3 协议进行安全管理。若要使用 HTTPS 协议，需要进行以下打印机设置。

 打印机中必须安装有证书和机密键。关于如何安装证书和机密键，请参考第 103 页上的创建并安装证书。  
 必须启用 HTTPS 协议。要启用 HTTPS 协议，需启用配置协议页面上的基于 web 的管理方式 ( 网络服务器 )的高级设置页面中的已使用 SSL 通信 ( 端口 443)。关于如何进入配置协议页面的详细信息，请参考第 92页上的配置协议设置。

![启用基于Web的管理方式并使用SSL通信(端口443)，建议使用特定版本浏览器访问。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7ef88d32cf29306c68f1cfc0fe31b958e04411cc93ab888942358cd6971c4de2.jpg)

# 注释

• Brother 建议 Windows® 用户使用 Microsoft® Internet Explorer® 6.0 ( 或更高版本 ) 或 Firefox 1.0 ( 或更高版本 )， Macintosh 用户使用 Safari 1.3 ( 或更高版本 )。无论使用何种浏览器，请确保始终启用JavaScript 和 Cookies。如果使用其他网络浏览器，请确保其与 HTTP 1.0 和 HTTP 1.1 兼容。若要使用网络浏览器，您需要知道打印服务器的 IP 地址。  
• Brother 建议您禁用 Telnet、FTP 和 TFTP 协议。使用这些协议访问本设备不安全。请参考第 92页上的配置协议设置。

打开您的网络浏览器。  
b 在您的浏览器中输入 “https://Common Name/”。(“Common Name” 为您签发证书的名称，例如 IP 地址。关于如何签发证书名称，请参考第 103 页上的创建并安装证书。 )

 例如：

https://192.168.1.2/ ( 如果证书名称为打印机的 IP 地址 )

![示例说明如何使用IP地址或DNS名称访问打印服务器，并提及证书签发与hosts文件编辑。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ea89f597bde701d14938e9556b0f1ec6a7e283d306d74e50275d5c13e78c5975.jpg)

# 注释

• 如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统，您也可以输入打印服务器的 DNS 名称。  
• 对于 Windows® 用户，因为打印服务器支持 TCP/IP 和 NetBIOS 名称，所以您也可以输入打印服务器的NetBIOS 名称。 NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68 页上的打印网络配置页。 NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为“BRNxxxxxxxxxxxx" ( 有线网络 ) 或 "BRWxxxxxxxxxxxx" ( 无线网络 )。

c 此时，您可以通过 HTTPS 协议使用打印机。

Brother 建议您同时使用安全管理 (SNMPv3) 和 HTTPS 协议。如果您使用 SNMPv3 协议，请遵循以下步骤。

![通过HTTPS协议使用打印机，并建议同时启用SNMPv3安全管理。可使用BRAdmin工具更改设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ca8c48a9bbbb46b9b92a926fb239ddd768989818f04285976ff9528d2e084b78.jpg)

# 注释

您也可以使用 BRAdmin 专业版 3 或 Web BRAdmin 更改 SNMP 设置。

点击网络配置。  
e 输入用户名和密码。默认用户名为 “admin”，默认密码为 “access”。  
f 点击配置协议。  
g 确保已启用 SNMP 设置，然后点击 SNMP 中的高级设置。  
h 您可以在以下屏幕上配置 SNMP 设置。

![SNMP设置界面，介绍三种SNMP操作模式，推荐使用SNMPv3以实现更安全的管理。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/29635c62c655ffa3846c476a8ba4aa424042b1b8d9a2d32d6b398de33538be47.jpg)

我们提供了三种 SNMP 操作模式。

#  SNMPv3 读写访问

在该模式下，打印服务器使用 SNMP 协议版本 3。如果您想安全管理打印服务器，请使用此模式。

![SNMPv3读写访问模式介绍及使用注意事项，支持通过特定工具管理打印服务器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/940109f39d8f5cc6833987992287533c7a7e2d261dcb4e6f4191d0031e9c720e.jpg)

# 注释

使用 SNMPv3 读写访问模式时，请注意以下几点：

• 您只能使用 BRAdmin 专业版 3、 Web BRAdmin 或网络基本管理 ( 网络浏览器 ) 管理您的打印服务器。  
• Brother 建议您使用安全 SSL 通信 (HTTPS)。

• 除 BRAdmin 专业版 3 和 Web BRAdmin 之外，其他所有使用 SNMPv1/v2c 的应用程序都受限制。若要允许使用 SNMPv1/v2c 应用程序，请使用 SNMPv3 读写访问和 v1/v2c 只读访问或 SNMPv1/v2c 读写访问模式。

#  SNMPv3 读写访问和 v1/v2c 只读访问

在该模式下，打印服务器采用 SNMP 协议版本 3 的读写访问以及版本 1 和版本 2c 的只读访问操作模式。

![SNMPv3读写与v1/v2c只读访问模式说明，适用于支持该模式的打印服务器及应用程序。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/f1c40d01bd17dca7140f32fbc63cfb7ab37279f1434020eef8c231fd2c5d91af.jpg)

# 注释

使用 SNMPv3 读写访问和 v1/v2c 只读访问模式时，由于某些访问打印服务器的 Brother 应用程序 (例如：BRAdmin Light) 授权版本 1 和版本 2c 只读访问，所以它们无法正常运行。如果您想使用所有应用程序，请使用 SNMPv1/v2c 读写访问模式。

#  SNMPv1/v2c 读写访问

在该模式下，打印服务器使用 SNMP 协议版本 1 和版本 2c。您可以使用所有 Brother 应用程序。但是，由于未进行用户验证且资料也未加密，所以这种模式不安全。

![SNMP Pv1/v2c模式下打印服务器的读写访问说明及BRAdmin专业版3的安全管理提示。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d5ec9e22deb099734799bca8251dec8b8dd097f90373f8b600fd17ad6a0d4e8a.jpg)

# 注释

如需获取更多信息，请参考网络基本管理中的“ 帮助 ” 文本。

# 使用 BRAdmin 专业版 3 的安全管理 ( 适用于 Windows®)

# 若要安全使用 BRAdmin 专业版 3 实用程序，您需要遵循以下几点。

 Brother 强烈建议您使用最新版本的 BRAdmin 专业版 3 实用程序或 Web BRAdmin，可登录以下网站：http://solutions.brother.com/ 下载。如果您使用低版本的 BRAdmin 1 实用程序管理 Brother 设备，用户验证将不安全。  
 如果您想避免从低版本的 BRAdmin 1 实用程序访问打印机，需通过网络基本管理 ( 网络浏览器 )，从配置协议页面上的 SNMP 的高级设置中禁用低版本的 BRAdmin 1 实用程序访问。请参考第 93 页上的使用网络基本管理（网络浏览器）的安全管理。  
 禁用 Telnet、FTP 和 TFTP 协议。使用这些协议访问本设备不安全。关于如何配置协议设置，请参考第 76页上的如何使用网络基本管理 ( 网络浏览器) 配置打印服务器设置。  
 如果您想同时使用 BRAdmin 专业版 3 和网络基本管理 ( 网络浏览器 )，请通过 HTTPS 协议使用网络基本管理。请参考第93页上的使用网络基本管理 ( 网络浏览器) 的安全管理。  
 如果您正在使用 BRAdmin 专业版 3 管理旧打印服务器 2 和新打印服务器混合组时，Brother 建议您在每组中使用不同的密码，以确保安全使用新的打印服务器。

BRAdmin 专业版比版本 2.80 低， Web BRAdmin 比版本 1.40 低，适用于 Macintosh 的 BRAdmin Light 比版本 1.10 低。  
2 NC-2000 系列、NC-2100p、NC-3100h、NC-3100s、NC-4100h、NC-5100h、NC-5200h、NC-6100h、NC-6200h、NC-6300h、NC-6400h、NC-8000、 NC-100h、 NC-110h、 NC-120w、 NC-130h、 NC-140w、 NC-8100h、 NC-9100h、 NC-7100w、 NC-7200w、 NC-2200w

# 安全功能锁 2.0 ( 适用于 HL-3070CW)

Brother 安全功能锁 2.0 通过限制 Brother 设备功能帮助您节约开支、增强安全性。

通过安全功能锁，您可以配置所选用户的密码、控制其使用某些或全部功能的权限或对其实行页数限制。这意味着只有经授权的用户才可以使用这些功能。

您可以使用网络浏览器配置和更改以下安全功能锁设置：

 PC 打印 1  
 USB 直接打印  
 彩色打印   
 页数限制  
 页码计数器 ( 仅供参考 )

1 如果您注册了计算机用户登录名，则无需输入用户密码即可限制 PC 打印。如需获取更多信息，请参考第 98页上的根据计算机用户登录名限制PC 打印。

# 如何使用网络基本管理 ( 网络浏览器 ) 配置安全功能锁 2.0

# 基本配置

a 在 HL-3070CW 网页上点击管理员设置，然后点击安全功能锁。

![配置HL-3070CW安全功能锁，开启功能锁并设置群组名/用户名及4位PIN码以限制打印权限。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9eeff070aae8ba6789f08653a9c008ea0da6f633405838fb7695ba6550b7114b.jpg)

b 将功能锁设置为开。  
c 在 ID 号码 /名称框内输入群组名或用户名，名称只能包含字母和数字，且长度不得超过 15 个字符。然后，在 PIN 码框内输入 4 位数的密码。

d 在打印框或其他框中取消选中您想限制的功能。如果您想配置最大页数，请在页数限制中选中开复选框，然后在最大框中输入数字。然后，点击提交。  
e 如果您想根据计算机用户登录名限制 PC 打印，请点击根据登录名限制 PC 打印并配置其设置。( 请参考下文的根据计算机用户登录名限制 PC 打印。 )

# 根据计算机用户登录名限制 PC 打印

通过配置此设置，打印机可根据计算机用户登录名进行验证，以允许在已注册的计算机上执行打印作业。

a 点击根据登录名限制 PC 打印，将出现根据登录名限制 PC打印屏幕。

![根据登录名限制PC打印设置：开启限制，输入用户登录名并选择对应ID号码。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ab78b404905ba1e7e6389a6a75a07892840f136d1fc92f3e7e74c77103262278.jpg)

b 将 PC打印限制设置为开。  
c 在登录名框内输入计算机用户登录名，然后在 ID 号码下拉列表中选择各登录名的 ID 号码，即选择您在基本配置的步骤中的ID号码/名称框中设置的ID号码。然后，点击提交。

![设置打印限制：输入计算机用户登录名，选择对应ID号码并提交；根据需求可按群组限制打印。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/23b4b900e750e0e549ad61ae763ddedbbe5b3831088825b567601ac76ea8508e.jpg)

# 注释

• 如果您想根据群组限制 PC 打印，请在群组中为所需的计算机登录名选择相同的 ID 号码。  
• 如果您正在使用计算机登录名功能，请务必确保已选中打印机驱动程序的使用 PC 登录名复选框。关于打印机驱动程序的更多信息，请参考随机光盘上的使用说明书。  
• 安全功能锁功能不支持 BRScript 打印机驱动程序打印。

# 设置公共模式

通过设置公共模式，您可以限制公共用户可用的功能。公共用户无需输入密码即可使用此设置所允许的功能。

a 在公共模式框中取消选中您想限制的功能的复选框。  
b 点击提交。

# 其他功能

您可以在安全功能锁 2.0 中设置以下功能：

#  重置所有的计数器

您可以通过点击重置所有的计数器重置页码计数器。

#  导出到 CSV 文件

您可以将包含 ID 号码 / 名称信息的当前页码计数器记录导出为 CSV 文件。

#  最后计数器记录

重置计数器后，本设备仍可进行页码计数。

![页码计数器功能介绍：支持导出CSV文件及重置后继续计数，推荐使用BRAdmin专业版3配置安全设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/4732e4328ff69d7da5e940758d2efd183c4274e4525606d86025a4523d8ae199.jpg)

# 注释

您可以使用 BRAdmin 专业版 3 配置安全功能锁 2.0，可登录以下网站：http://solutions.brother.com/ 下载。该实用程序仅适用于 Windows® 用户。

# 使用 IPPS 安全打印文档

若要在网络上安全打印文档，您可以使用 IPPS 协议。

![介绍从指定网址下载适用于Windows的IPPS安全打印文档方法及注意事项。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c588245bbb8d3995e68a87f964a69b8f78e58bd80091cbf06266f1faa89a4154.jpg)

# 注释

• 使用 IPPS 信息互通时，不能阻止未经授权的用户访问打印服务器。  
• IPPS 适用于 Windows® 2000/XP、 Windows Vista® 、 Windows® 7 和 Windows Server® 2003/2008。

若要使用 IPPS 协议，需要进行以下打印机设置：

 打印机中必须安装有证书和机密键。关于如何安装证书和机密键，请参考第 103 页上的创建并安装证书。

 必须启用 IPPS 协议。若要启用 IPPS 协议，请启用配置协议页面上的 IPP 的高级设置页面中的已使用SSL通信 ( 端口 443)。关于如何进入配置协议页面的详细信息，请参考第 92 页上的配置协议设置。

IPPS 打印与 IPP 打印的步骤基本相同。有关详细信息，请参考第 12 章的在 Windows® 操作系统下进行网络打印。

# 指定一个不同的 URL

敬请注意，您可以根据需要在 URL 栏中输入以下地址：

```txt
https://Common Name/ipp 
```

这是默认的 URL， Brother 建议您使用此 URL。

```txt
https://Common Name/ipp/port1 
```

此 URL 与 HP Jetdirect 兼容。

```txt
https://Common Name/ 
```

![图片展示了如何使用URL与HP Jetdirect兼容的打印机进行连接，包括完整和简化的URL格式说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a16c635fef6fdf54b22a37733f4f0d5f0fbcd947ddbde43a4d09b031f0b3f903.jpg)

# 注释

如果您忘记了 URL 的详细信息，可以简单输入上述文本 (https://Common Name/)，打印机仍可接收并处理数据。

“Common Name” 为您签发证书的名称，例如 IP 地址。关于如何签发证书名称，请参考第 103页上的创建并安装证书。

 例如：

https://192.168.1.2/ ( 如果证书名称为打印机的 IP 地址。 )

# 使用带用户验证的电子邮件通知

若要通过需用户验证的 SMTP 安全服务器使用电子邮件通知功能，您必须使用 POP 优先于 SMTP 或 SMTP-AUTH 方法。这些方法可防止未经授权的用户访问邮箱服务器。您可以使用网络基本管理 ( 网络浏览器 )、BRAdmin 专业版 3 和 Web BRAdmin 来配置这些设置。

![配置邮箱服务器访问权限及验证设置，需与邮件服务器匹配，并建议咨询网络管理员。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/632cd2314dd97cfa967b26b2bf924ae067cc741e915aff39f51a70ed6b0c6f84.jpg)

# 注释

您必须使 POP3/SMTP 的验证设置与一个电子邮件服务器的设置相匹配。关于使用前如何进行配置的详细信息，请联系网络管理员或网络服务提供商。

# 如何使用网络基本管理 ( 网络浏览器 ) 配置 POP3/SMTP 设置

打开您的网络浏览器。  
b 在您的浏览器中输入 “http://printer's IP address/” (“printer's IP address” 为打印机的IP 地址 )。

 例如：

http://192.168.1.2/

![访问打印机网页配置界面的方法：输入打印机IP地址或DNS名称，支持TCP/IP协议。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/af410b94e2c11d975bc6e7ffec0cd979aa698c305fa4faa330727638e7de90f1.jpg)

# 注释

• 如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统，您也可以输入打印服务器的 DNS 名称。  
• 对于 Windows® 用户，因为打印服务器支持 TCP/IP 和 NetBIOS 名称，所以您也可以输入打印服务器的NetBIOS 名称。 NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68页上的打印网络配置页。 NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为“BRNxxxxxxxxxxxx" ( 有线网络 ) 或 "BRWxxxxxxxxxxxx" ( 无线网络 )。

c 点击网络配置。  
d 输入用户名和密码。默认用户名为 “admin”，默认密码为 “access”。  
e 点击配置协议。  
f 确保已启用 POP3/SMTP 设置，然后点击 POP3/SMTP 中的高级设置。

# g 您可以在此页面上配置 POP3/SMTP 设置。

![配置邮件客户端的POP3/SMTP设置，包括启用服务及高级设置选项。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7d4c9e439687f5a1764884ff32f7c0b7f9584c31a277eb4c88d204abc4dcaa7c.jpg)

![配置POP3/SMTP设置界面，展示邮件服务器、端口号等参数输入示例。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/af01fce2718d921ecd1533300cdf920ca6a2c0d13e08f63e262dea24c9d44d0b.jpg)

# 注释

• 您也可以使用网络基本管理更改 SMTP 端口号。如果您的 ISP ( 因特网服务提供商 ) 提供 “OutboundPort 25 Blocking (OP25B)” 服务，这将很有帮助。通过将 SMTP 端口号更改为您的 ISP 使用的指定的SMTP 服务器端口号 ( 例如，端口 587)，即可通过 SMTP 服务器发送电子邮件。您还需要在 SMTP 服务器认证方法中选择 SMTP-AUTH 以启用 SMTP 服务器验证。  
• 如果 POP 优先于 SMTP 和 SMTP-AUTH 均可用， Brother 建议您使用 SMTP-AUTH。  
• 如果您选择 POP 优先于 SMTP 作为 SMTP 服务器认证方法，则必须配置 POP3 设置。您也可以使用APOP 方法。  
• 如需获取更多信息，请参考网络基本管理中的 “ 帮助 ” 文本。  
• 配置完成后，通过发送测试电子邮件可以确认电子邮件设置是否正确。

h 配置完成后，点击提交。出现测试电子邮件发送 / 接收配置对话框。  
i 如果您想使用当前设置进行测试，请遵循屏幕上的指示执行操作。

# 创建并安装证书

通过配置证书和相对应的机密键， Brother 打印服务器允许您使用 SSL/TLS 信息互通。该打印服务器能支持两种证书。一种为自我认定证书，另一种为由 CA 机构 ( 证书授权中心 ) 颁发的证书。

#  使用自我认定证书

该打印服务器可颁发自我认定证书。使用该证书，可以在不需要 CA 认证证书的情况下简便地使用SSL/TLS 信息互通。请参考第 105页上的创建和安装自我认定证书。

#  使用 CA 认证证书

有两种方法安装 CA 认证证书。若已经存在 CA 认证证书，或者希望使用外部 CA 认证证书：

• 当使用打印服务器的 CSR ( 证书签订请求 ) 时，请参考第 118 页上的创建 CSR 并安装证书。  
• 当导入证书和机密键时，请参考第 120 页上的导入和导出证书和机密键。

![图片标题：打印服务器CSR与证书操作指南及SSL/TLS使用建议这个标题简要概括了图片中的主要内容，包括关于如何处理CSR、安装和导入证书的操作指引，以及使用SSL/TLS时的建议。同时，它也符合您要](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a15f2bbd8f179c707e111bacf6b81f5616a40a4dc3ad80063a6f5238a5ad2b20.jpg)

# 注释

• 如果您要使用 SSL/TLS 信息互通， Brother 建议您在使用之前先联系系统管理员。  
• 该打印服务器仅储存您已安装或事先导入的一对证书和一个机密键。若您安装新的证书，原先打印机上的证书及个人密码将被覆盖。  
• 当您将打印服务器恢复为出厂默认设置时，已安装的证书和机密键将被删除。如果您希望重设打印服务器后仍然保留原有的证书和机密键，那么请在重设打印服务器之前先将其导出，然后重新安装。请参考第 120 页上的如何导出证书和机密键。

此功能仅可以使用网络基本管理 (网络浏览器 ) 进行配置。使用网络基本管理访问配置证书页面时，请遵循以下步骤：

打开您的网络浏览器。

b 在您的浏览器中输入 “http://printer's IP address/”(“printer's IP address” 为打印机的IP 地址 )。

 例如：

http://192.168.1.2/

![访问打印机网页配置界面的方法：输入打印机IP地址或DNS名称，如http://192.168.1.2/。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bb6e2c1642fa4393f6321b1b75db706fd693cc41842f2c1a0fc67b12b9cfc941.jpg)

# 注释

• 如果您已在计算机上编辑了 hosts 文件，或者正在使用域名系统，您也可以输入打印服务器的 DNS 名称。  
• 对于 Windows® 用户，因为打印服务器支持 TCP/IP 和 NetBIOS，所以您也可以输入打印服务器的NetBIOS 名称。 NetBIOS 名称可以在网络配置页上找到。关于如何打印网络配置页，请参考第 68页上的打印网络配置页。 NetBIOS 名称为节点名称的前 15 个字符，默认状态下显示为“BRNxxxxxxxxxxxx" ( 有线网络 ) 或 "BRWxxxxxxxxxxxx" ( 无线网络 )。

c 点击网络配置。

d 输入用户名和密码。默认用户名为 “admin”，默认密码为 “access”。

e 点击确定。

f 点击配置证书。  
g 您可以在以下屏幕中配置证书设置。

![网络配置界面：输入默认用户名和密码后，进行证书设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/057353c2dd1e8a7141ed3965ae5b28e8e1a7fb1a676a1b0c92f92e0deff3f050.jpg)

![证书配置界面，展示可配置选项及状态，灰色表示功能不可用。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/f37622705df5f37a4c6170a38038cfa899d4a7e54d8f08a663718e2fc0ee419b.jpg)

# 注释

• 无法使用的功能会显示为灰色和无法连接的状态。  
• 如需获取关于配置的更多信息，请参考网络基本管理中的 “ 帮助 ” 文本。

# 创建和安装自我认定证书

# 如何创建和安装自我认定证书

a 在配置证书页面上点击创建自我认定证书。  
b 输入名称和有效日期，然后点击提交。

![创建和安装自我认定证书步骤及注意事项，包括命名规则和用途说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/96e861d5fec26d16872e4228464b945cf77d72ebeeffacb676a4368443aebc78.jpg)

# 注释

• 名称需少于 64 个字节。当通过 SSL/TLS 信息互通使用打印机时，请输入标识符，例如 IP 地址、节点名称及域名。在默认状态下显示节点名称。  
• 如果您使用 IPPS 或 HTTPS 协议并在 URL 中输入了与用于自我认定证书的名称不同的名称，将弹出警告窗口。

c 此时自我认定证书创建成功。  
d 请遵循屏幕上的提示配置其他安全设置。  
e 重启打印机以激活配置。  
f 此时自我认定证书将保存在您的打印机内存中。若要使用 SSL/TLS 信息互通，必须在您的计算机中也安装自我认定证书。请阅读以下部分。

# 如何在计算机中安装自我认定证书

![如何在计算机中安装打印机自我认定证书的步骤说明，适用于IE 6.0及其它浏览器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c10c1be400387b0d17cc560ce9f3294527b54047202cd59ced0952824a81cfe0.jpg)

# 注释

以下步骤适用于 Microsoft® Internet Explorer® 6.0。如果您使用其他网络浏览器，请遵循网络浏览器上的“ 帮助 ” 文本。

# 对于有管理员权限的 Windows Vista® 和 Windows® 7 用户

点击 按钮和所有程序。

b 右击 Internet Explorer，然后点击以管理员身份运行。

![以管理员身份运行Internet Explorer的步骤及用户帐户控制提示确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/65aab07661683644b45e971ec98fbf9a1f62743fb724133acbe0020f75cb8d50.jpg)

![以管理员身份运行程序后，根据Windows版本点击继续或确认，并在浏览器中输入打印机IP地址。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a9a1a812c10e77b9c7f35a7ee9efed74e0856266929d1aba88ad5af5ebc49615.jpg)

# 注释

当出现用户帐户控制屏幕时：

(Windows Vista®) 点击继续。

(Windows® 7) 点击是。

c 在您的浏览器中输入 “http://printer's IP address/” (“printer's IP address” 为打印机的IP 地址或节点名称 )。

然后，点击继续浏览此网站 ( 不推荐 )。

![输入打印机IP访问，忽略证书错误并继续浏览，详情参见第114页。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/36bad3c7e073bf2f31a802a63e75a04ab5d375f2a6e50e4cd69cedf8cba1deee.jpg)

d 点击证书错误，然后点击查看证书。关于其他指示，请参考第 114页上的步骤 d 及之后的内容。

![处理证书错误并以管理员身份运行IE的步骤说明](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8ce669b4f2f3567f647d51f110003524749bd9b7f16674a8c8b07757a8415bf6.jpg)

对于没有管理员权限的 Windows Vista® 和 Windows® 7 用户

点击 按钮和所有程序。  
b 右击 Internet Explorer，然后点击以管理员身份运行。

![对于无管理员权限的Vista和Win7用户，指导如何以管理员身份运行IE并输入密码。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7176c6497093cffcf7b35a4f87c2169e212089c78b8798c62b526f3184ae2e04.jpg)

c 选择您安装时要使用的管理员，输入管理员密码，然后点击确定或是。

![输入管理员密码后确定，再通过浏览器访问打印机IP地址继续设置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/03f77fa267a5603784c746f91315aebc952870991ce3594fdf60273b392aef7e.jpg)

在您的浏览器中输入 “http://printer's IP address/” (“printer's IP address” 为打印机的IP 地址或节点名称 )。

然后，点击继续浏览此网站 ( 不推荐 )。

![访问打印机IP地址后，忽略安全警告并继续浏览，接着查看证书错误详情。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/0f94c909d821c911cfcb34ab5e5bb980e5bfbe41d6031830449164ce2511dd1d.jpg)

e 点击证书错误，然后点击查看证书。

![点击证书错误查看证书，选择详细信息选项卡并复制到文件。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b1363f5b4a23a64b65c1aaeebf070dd49b046b6576739214f746ba808fa7f736.jpg)

f 选择详细信息选项卡，然后点击复制到文件 ...。

![选择详细信息选项卡，点击复制到文件后，按下一步继续操作。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/09cf340f50673b8411398ae5de4251fd4d912b3475959c5b81db022fd4b00936.jpg)

# 点击下一步。

![选择DER编码二进制X.509(.CER)证书格式，并继续下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/dd68c9ced2949b14587ab4ed3b713e324bcb189009265455c5cc238563966275.jpg)

# h 确保选中 DER 编码二进制 X.509 (.CER)，然后点击下一步。

![选择DER编码二进制X.509(.CER)格式后，点击浏览以选择证书文件。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e73f602025b08a050038f7a0aaac8d5dc861bc52571f89c02d0ee783bd16dfab.jpg)

# i 点击浏览。

![点击下一步后，选择浏览文件夹以指定目标位置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/647de26bd53abe36e339434e91a4c250cfe5d1ba6c36288e3948c43f9acaea1f.jpg)

# j 点击浏览文件夹。

![选择保存证书文件的文件夹，并输入文件名后点击保存。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ca954ceb423bc3f91bbf05836f1c9bccb40da2abf1617a52aa3768d6e5615117.jpg)

# k 选择您想保存证书文件的文件夹，输入文件名，然后点击保存。

![选择保存证书文件的位置与命名，示例展示了保存至桌面的过程。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7c992a74077c71f6cab1e638dc9ff5d72b4df51af5c2a209fecd73e5521c461c.jpg)

![输入文件名保存证书，选择桌面则保存至管理员桌面。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/347bea198d30f82c701143d97e4486865f392aac48d6d006d94f502c5cba6cf7.jpg)

# 注释

如果您选择桌面，证书文件将保存到您所选择的管理员的桌面。

# l 点击下一步。

![证书安装向导：选择保存位置后，点击下一步完成安装。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b3b70e4e1a0d3511d0897963f4b27435f1692ffa19c900124e0bf46edded7687.jpg)

# m 点击完成。

![点击下一步后，按照提示完成设置，并点击确定以继续安装过程。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bf5a80f1c3d9e3329a45af610f0382534e3587f8ac37882166190dba6c44dbdd.jpg)

# n 点击确定。

![点击完成设置后，确认操作以继续进行下一步配置。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c216d2e4e53037e47b07a842ab9d89b4fdd2dfb002359003b8f2d8696edc4405.jpg)

# o 点击确定。

![点击确定后，打开指定文件夹并双击证书文件以继续安装过程。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/b608256e64bb798d61f452cfc59754414102d75d81e0cd4f3011b1e574b2cb43.jpg)

p 打开您在步骤 k 中选择的用于保存证书文件的文件夹，然后双击证书文件。关于其他指示，请参考第109页上的步骤 d 及之后的内容。

![打开证书文件并根据指示操作；Windows用户需通过浏览器访问打印机IP地址。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/12441559dd8669421693155f0f5afb239ac6925a390a8fb34b435143f8154e18.jpg)

对于 Windows® 2000/XP 和 Windows Server® 2003/2008 用户：

打开您的网络浏览器。  
b 在您的浏览器中输入 “http://printer's IP address/” (“printer's IP address” 是您为证书指定的 IP 地址或节点名称 )。  
c 出现以下对话框时，点击查看证书。

![访问打印机IP地址后，点击查看并安装证书的步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/1be5607a8a26e31df40279ad74eff9a68c6570e424c6016e41002ac52bf95130.jpg)

d 在常规选项卡中点击安装证书 …。

![在常规选项卡中点击安装证书，出现证书导入向导时点击下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/00507441b018af0c0296e4c03d3f6ae6832cdf853c421ce2967e593c4de9adad.jpg)

e 出现证书导入向导时，点击下一步。

![证书导入向导：选择存储区并点击浏览以继续下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/8e514bb95f07f2bf5283c88271a4f4fb30f7f065faf176e4d1995789229d5ef3.jpg)

f 选中将所有的证书放入下列存储区，然后点击浏览。

![将所有证书导入至受信任的根证书颁发机构存储区的操作步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c47738564e95088e0c03359687f0f36cc12c04a11321bdbb1d7f8692aedf2845.jpg)

g 选择受信任的根证书颁发机构，然后点击确定。

![选择受信任的根证书颁发机构后，点击确定，然后点击下一步。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7c6702f84783c495b5960eaa0543a3c525b22e9f7cfc9455151be90dad935442.jpg)

# h 点击下一步。

![点击确定后，进入下一步设置界面，准备进行最终确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/e268f15dae153ea1e54c75be1df6d485bbee658482aea24c8047844f49eb84f9.jpg)

# i 点击完成。

![点击下一步后，根据提示完成设置；若指纹验证正确，则点击“是”确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/c3d360c6ca3ab81aa839147fd7155dfe0d694d1f84e1552cc8b09b57f164984a.jpg)

# j 如果指纹 ( 拇指纹 ) 正确，点击是。

![指纹验证步骤：展示拇指按压指纹识别区域，若指纹匹配成功，则点击“是”确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/99788b983647a48477d1cce333970ab40334d667fca47b3d99524a3b25d3b7d1.jpg)

![拇指指纹验证通过，点击“是”确认打印网络配置页。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/9d0910605c9301c18003a4a886e682d09b06fabd15a1776ac2ef8889854f0076.jpg)

# 注释

指纹 ( 拇指纹 ) 将打印在网络配置页上。关于如何打印网络配置页，请参考第 68页上的打印网络配置页。

k 点击确定。

![图片标题：网络配置页打印及SSL/TLS证书安装指南，含创建CSR步骤说明。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/f37692537b0f6397bd4999adb3ec1300515a805c773c71b5f9d3b795d44e9ebc.jpg)

l 此时在您的计算机上已安装自我认定证书， SSL/TLS 信息互通即可使用。

# 创建 CSR 并安装证书

# 如何创建 CSR

在配置证书页面上点击创建 CSR。  
b 输入名称和您的个人信息，如组织，然后点击提交。

![创建CSR并安装证书步骤及注意事项，包括输入个人信息、名称限制和建议预先安装根证书。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/ca4d2d88b6c11e9068604e424a3c139c5c59f8075846e9a858faf5763e5b3f21.jpg)

# 注释

• Brother 建议您在创建 CSR 之前，在您的计算机上安装由 CA 认证的根证书。  
• 名称需少于 64 个字节。当通过 SSL/TLS 信息互通使用打印机时，请输入标识符，例如 IP 地址、节点名称及域名。在默认状态下显示节点名称。名称为必填项。  
• 如果您在 URL 中输入了与证书使用的名称不同的名称，将弹出警告窗口。  
• 组织、组织单位、城市 / 位置和自治区 /省份的名称需少于 64 个字节。  
• 国家 / 区域应由两个字符的 ISO 3166 国家代码组成。

c 显示 CSR 内容时，点击保存，将 CSR 文件保存在您的计算机中。  
d 至此， CSR 创建完成。

![图片标题：说明CSR文件保存步骤及注意事项，包括ISO 3166国家代码格式要求和向CA发送CSR的建议。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/312b8d077d85c6070a2793fffe85950687f3c30126de88c5c888f9205f5f1281.jpg)

# 注释

• 关于将 CSR 发送到 CA 认证的方法，请遵循 CA 认证政策。  
• 如果您正在使用 Windows Server® 2003/2008 的企业根 CA，Brother 建议您在创建证书时，使用证书模板中的 Web 服务器。如需获取更多信息，请登录以下网站：http://solutions.brother.com/。

# 如何将证书安装在打印机中

当您接收到 CA 授予的证书时，请遵循以下步骤将证书安装在打印服务器中。

![如何将CA授予的证书安装到打印机中，包括访问指定网站获取更多信息及具体安装步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/412ce0573c807f4f802b9c229257139470e91065d307a82a6f94fcffd27d88b7.jpg)

# 注释

只能安装由该打印机 CSR 授予的证书。

a 在配置证书页面上点击安装证书。  
b 指定由 CA 认证的证书文件，然后点击提交。  
c 此时证书创建成功。  
d 请遵循屏幕上的提示配置其他安全设置。  
e 重启打印机以激活配置。  
f 此时，证书保存在您的打印机中。若要使用 SSL/TLS 信息互通，必须在您的计算机中也安装 CA 认证的根证书。有关安装的详细信息，请联系网络管理员。

# 导入和导出证书和机密键

# 如何导入证书和机密键

a 在配置证书页面上点击输入证书及机密键。  
b 指定您想导入的文件。  
c 如果文件加密，请输入密码，然后点击提交。  
d 此时证书和机密键导入成功。  
e 请遵循屏幕上的提示配置其他安全设置。  
f 重启打印机以激活配置。

此时证书和机密键已导入到您的打印机。若要使用 SSL/TLS 信息互通，必须在您的计算机中也安装 CA认证的根证书。有关安装的详细信息，请联系网络管理员。

# 如何导出证书和机密键

a 在配置证书页面上点击输出证书及机密键。  
b 如果您想加密文件，请输入密码。

![导出证书与密钥步骤：点击输出、设置密码（可选）、确认密码、选择保存位置，完成导出。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/068f7e4ff85fd4eee092099d58eabda349d0d65dce5ff6f1cbd2264cb05e759e.jpg)

# 注释

如果使用空白密码，则输出不会加密。

c 重新输入密码以进行确认，然后点击提交。  
d 指定您要保存文件的位置。  
e 此时证书和机密键已导出至您的计算机。

![图片展示了导出证书和密钥的步骤，包括确认密码、选择保存位置，并提到可导入已导出文件。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/6bd34ce757b21edaa375cd433edbe7636fcfba44d441f0b4078cce5d9f47a221.jpg)

# 注释

您可以导入已导出的文件。

# 15 故障排除

# 概述

本章阐述如何解决您在使用本设备时可能遇到的常见故障。如果您阅读本章后仍无法解除故障，请登录以下网站访问 Brother Solutions Center (Brother 解决方案中心 )：http://solutions.brother.com/。

本章共有以下几个部分：

 常见问题  
 网络打印软件安装问题  
 打印问题  
 与协议相关问题的故障排除方法  
 无线网络故障排除 ( 适用于 HL-3070CW)

# 常见问题

插入随机光盘后，不能自动开始播放。

如果您的计算机不支持 Autorun ( 自动运行 )，插入光盘后将不能自动播放菜单。此时，请在光盘的根目录中执行 start.exe。

# 如何将 Brother 打印服务器恢复为出厂默认设置

您可以将打印服务器恢复为出厂默认设置 ( 重置密码和 IP 地址等所有信息 )( 请参考第 67 页上的将网络设置恢复为出厂默认设置)。

计算机搜索不到设备 / 打印服务器。

无法连接到设备 / 打印服务器。

设备 / 打印服务器在 Remote Setup、 BRAdmin Light 或 BRAdmin 专业版 3 窗口中不显示。

计算机上的防火墙设置可能阻断了必要的网络连接。此时，您需要禁用计算机上的防火墙并重新安装驱动程序。

Windows® 7 用户 :

点击 按钮、控制面板、系统和安全，然后点击 Windows 防火墙。确保 Windows 防火墙状态设置为关闭。

Windows Vista® 用户：

1) 依次点击 按钮、控制面板、网络和 Internet、 Windows 防火墙和更改设置。

2) 出现用户帐户控制屏幕时，执行以下操作：

• 具有管理员权限的用户：点击继续。  
• 不具有管理员权限的用户：输入管理员密码并点击确定。

3) 点击常规选项卡。确保已选择关闭 ( 不推荐 )。

4) 点击确定。

![设置网络选项时，根据用户权限点击继续或输入密码，并选择关闭选项后确认。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/1bf26b11cfa0ca113d679f7ee8e69937f1a421704f0ac0f2f6178b1bec329c72.jpg)

# 注释

安装了 Brother 软件包后，重新启动防火墙。

# Windows® XP SP2/SP3 用户：

1) 依次点击开始按钮、控制面板、网络和 Internet 连接。  
2) 双击 Windows 防火墙。  
3) 点击常规选项卡。确保已选择关闭 ( 不推荐 )。  
4) 点击确定。

![关闭Windows防火墙设置步骤及安装Brother软件后的防火墙重启提示](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/51eb83d6265c6508c3398df5780d1a4b069f144d513d062f4aa37e07ca35c871.jpg)

# 注释

安装了 Brother 软件包后，重新启动防火墙。

# 网络打印软件安装问题

在网络打印软件安装过程中或在 Windows® 中的 Brother 设备的打印机驱动程序安装中没有找到 Brother打印服务器。使用 Mac OS X 的简单网络配置功能时没有找到 Brother 打印服务器。

 对于使用以太网电缆连接的网络

在安装网络打印软件或打印机驱动程序之前，确保您已经根据本使用说明书的第 2 章中的说明完成Brother 打印服务器的 IP 地址设置。

 对于无线网络

在安装网络打印软件或打印机驱动程序之前，确保您已经根据本使用说明书的第 3 章中的说明完成Brother 打印服务器的 IP 地址设置和无线网络设置。

请进行以下检查：

a 确保设备电源已打开、连接至网络并准备好打印。  
b 检查您的网络连接状态。

对于有线网络用户：

检查指示灯是否正在运行。设备的后面板上有两个 Brother 打印服务器指示灯。上方的橙色指示灯显示速度状态。下方的绿色指示灯显示连接/ 运行 ( 接收 / 发送) 状态。

![Brother打印服务器指示灯说明：橙色灯示速度，绿色灯示连接/运行状态。橙灯亮表示100BASE-TX，熄灭则为10BASE-T。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3bc91387cf8783f82abea6a7daecde37f6dde3a5c411967a9745046b0eed4f3d.jpg)

 上方指示灯显示为橙色：当打印服务器连接到 100BASE-TX 快速以太网时，速度指示灯显示为橙色。  
 上方指示灯熄灭：当打印服务器连接到 10BASE-T 以太网时，速度指示灯熄灭。  
 下方指示灯显示为绿色：打印服务器连接到以太网时，连接 / 运行指示灯显示为绿色。  
 下方指示灯熄灭：打印服务器没有连接到网络时，连接 / 运行指示灯熄灭。

对于无线网络用户 ( 适用于 HL-3070CW)：

![指示灯状态说明：绿色表示已连接以太网，熄灭表示未连接；无线网络需检查信号强度。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/d15ae01a9a17ca2e7992d75059c27ff88c8835f06533e0d7adeedf08a7a147ef.jpg)

# 注释

确保已经启用设备的无线网络设置。

在基础架构模式下，检查设备处于准备就绪或休眠模式时液晶显示屏上的无线网络信号是否显示为：( 强 )/ ( 中 )/ ( 弱 )。

如果是，则表明您的设备已连接到无线网络。

如果信号显示为 ( 无 )，则表明您的设备未连接到无线网络。若要配置无线网络设备，请参考第 3 章的配置无线网络设备 ( 适用于 HL-3070CW)。

![图片说明了设备连接无线网络的状态显示及未连接时的特殊情况，包括开放系统验证下的显示。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/99af9f5fe41291d40ca1a259efc0bce5b590fc282fa3651c0e12c2a8176824ce.jpg)

# 注释

在下列状态下，即使您的设备未连接到无线网络，无线网络信号 也会显示在液晶显示屏上。

您的设备连接到具有开放系统验证的接入点。

c 打印网络配置页并检查 IP 地址等设置是否与网络相匹配。不匹配或两个重复的 IP 地址可能导致故障。确定 IP 地址已经正确载入打印服务器，并确保网络中没有其他节点使用该 IP 地址。关于如何打印网络配置页的说明，请参考第 68 页上的打印网络配置页。  
d 如下所述确定网络中的打印服务器：

 对于 Windows® 用户

1 点击开始、所有程序 1、附件，然后选择命令提示符。

1 对于 Windows® 2000 用户，此处为程序

2 请根据主机操作系统命令提示输入命令查验打印服务器：

ping ipaddress

ipaddress 为打印服务器的 IP 地址 ( 请注意：在某些情况下，打印服务器设置 IP 地址后大约需要 2 分钟载入 IP 地址 )。

 对于 Mac OS X 10.3.9 或更高版本用户

1 在运行菜单中选择应用程序。  
2 打开实用程序文件夹。  
3 双击终端图标。  
4 请根据终端窗口提示输入命令查验打印服务器：

ping ipaddress

ipaddress 为打印服务器的 IP 地址 ( 请注意：在某些情况下，打印服务器设置 IP 地址后大约需要 2 分钟载入 IP 地址 )。

e 如果您已尝试执行了上述步骤 a 到 d 但问题仍然存在，请将打印服务器恢复为出厂默认设置，然后通过初始设置再试一次。关于如何恢复出厂默认设置，请参考第 67 页上的将网络设置恢复为出厂默认设置。  
f 如果安装失败，可能因为您计算机上的防火墙阻断了与设备必要的网络连接。此时，您需要禁用计算机上的防火墙并重新安装驱动程序。如需获取更多信息，请参考第 121 页上的常见问题。如果您正在使用个人防火墙软件，请参考软件附带的使用说明书或联系软件制造商。

# 打印问题

无法打印打印作业。

检查打印服务器的状态和配置。

a 确保设备电源已打开、连接至网络并准备好打印。  
b 打印设备的网络配置页并检查 IP 地址等设置是否与网络相匹配。不匹配或两个重复的 IP 地址可能导致故障。确定 IP 地址已经正确载入打印服务器，并确保网络中没有其他节点使用该 IP 地址。关于如何打印网络配置页的说明，请参考第68 页上的打印网络配置页。  
c 如下所述确定网络中的打印服务器：

#  对于 Windows® 用户

1 点击开始、所有程序 1、附件，然后选择命令提示符。

对于 Windows® 2000 用户，此处为程序

2 请根据主机操作系统命令提示输入命令查验打印服务器：

ping ipaddress

ipaddress 为打印服务器的 IP 地址 ( 请注意：在某些情况下，打印服务器设置 IP 地址后大约需要 2 分钟载入 IP 地址 )。

3 如果成功接收到回复，请转到第 126 页上的 Windows® 2000/XP、 Windows Vista® 、 Windows® 7和Windows Server2003/2008 IPP故障排除。否则，请转到步骤。

#  对于 Mac OS X 10.3.9 或更高版本用户

1 在运行菜单中选择应用程序。  
2 打开实用程序文件夹。  
3 双击终端图标。  
4 请根据终端窗口提示输入命令查验打印服务器：

ping ipaddress

ipaddress 为打印服务器的 IP 地址 ( 请注意：在某些情况下，打印服务器设置 IP 地址后大约需要 2 分钟载入 IP 地址 )。

5 如果成功接收到回复，请转到步骤 d。

d 如果您尝试执行了上述步骤a到c但问题仍然存在，请将打印服务器恢复为出厂默认设置，然后通过初始设置再试一次。关于如何恢复出厂默认设置，请参考第 67 页上的将网络设置恢复为出厂默认设置。

# 打印过程中发生错误

当其他用户正在打印大量数据 ( 如打印很多页或大量高分辨率的图形页面 ) 时，如果您试图进行打印，则只有当打印机完成当前打印后才能接受您的打印作业。如果您的打印作业等待时间超出一定限度，则将发生超时并出现错误信息。在这种情况下，请在其他作业结束后重新进行打印作业。

# 与协议相关问题的故障排除方法

# Windows® 2000/XP、 Windows Vista® 、 Windows® 7 和 Windows Server®2003/2008 IPP 故障排除

我想使用除端口 631 以外的端口号。

如果您使用端口 631 进行 IPP 打印，则会发现防火墙不允许打印数据通过。在这种情况下，请使用另外的端口号 (端口 80)，或配置您的防火墙使其允许端口 631 的数据通过。

若要使用 IPP 将打印作业发送到使用端口 80 ( 标准 HTTP 端口 ) 的打印机，在配置 Windows® 2000/XP、Windows Vista® 、 Windows® 7 与 Windows Server® 2003/2008 系统时请输入以下信息：

http://ipaddress/ipp

无法选中 Windows® XP 、 Windows Vista® 和 Windows® 7 中的 “ 转到打印机网站 ” 选项。无法选中Windows® 2000 和 Windows Server® 2003/2008 中的 “ 获取更多信息 ” 选项。

如果您正在使用以下 URL：

http://ipaddress:631 ? http://ipaddress:631/ipp，

Windows® 2000/XP、Windows Vista® 、Windows® 7 和 Windows Server® 2003/2008 中的获取更多信息选项将不可用。若要使用获取更多信息选项，请使用以下 URL：

http://ipaddress。

这一操作将迫使 Windows® 2000/XP、Windows Vista® 、Windows® 7 和 Windows Server® 2003/2008 使用端口 80 与 Brother 打印服务器通信。

# 网络基本管理 ( 网络浏览器 ) 故障排除 (TCP/IP)

a 如果使用您的网络浏览器无法连接到打印服务器，请检查浏览器的代理服务器设置。查看例外设置，必要时输入打印服务器的 IP 地址。当您每次想查看打印服务器时，此设置将阻止计算机连接到 ISP 或代理服务器上。  
b 确保您使用合适的网络浏览器，Brother 建议 Windows® 用户使用 Microsoft® Internet Explorer® 6.0 ( 或更高版本 ) 或者 Firefox 1.0 ( 或更高版本 )， Macintosh 用户使用 Safari 1.3 ( 或更高版本 )。无论使用何种浏览器，请确保始终启用 JavaScript 和 Cookies。如果使用其他网络浏览器，请确保其与 HTTP 1.0和 HTTP 1.1 兼容。

# 无线网络故障排除 ( 适用于 HL-3070CW)

![确保启用JavaScript和Cookies，浏览器需兼容HTTP 1.0/1.1。介绍HL-3070CW无线网络故障排除及连接问题。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/36aefa04ee047229de03bf4e43541267238bf1af226c262208c06034c6e748ed.jpg)

# 注释

如果您想确认无线网络状态，请参考第 123 页上的 b。

# 无线连接问题

# 无线网络连接有时会被禁用。

无线网络连接状态会受 Brother 打印机和其他无线设置所处环境的影响。下列状况可能会引起连接问题：

 Brother 设备和接入点 / 路由器间存在混凝土或金属结构的墙体。  
 网络附近存在电视机、计算机设备、微波炉、对讲机、移动 / 便携式电话、充电器、交流电源适配器等电器设备。  
 网络附近存在广播电台或高压线。  
 打开或关闭附近的日光灯时。

# A 附录

# 使用服务

此服务是可通过打印至 Brother 打印服务器的计算机访问的一种资源。Brother 打印服务器提供以下预约的服务 ( 在 Brother 打印服务器远程控制台执行 SHOW SERVICE 命令，查看可用服务列表 )：在命令提示符栏中输入 HELP，获取支持命令的列表。

<table><tr><td>服务(实例)</td><td>定义</td></tr><tr><td>BINARY_P1</td><td>TCP/IP 二进制</td></tr><tr><td>TEXT_P1</td><td>TCP/IP 文本服务(在每次换行前添加回车)</td></tr><tr><td>PCL_P1</td><td>PCL 服务(切换 PJL-兼容打印机到 PCL 模式)</td></tr><tr><td>BRNxxxxxxxxxxxxx</td><td>TCP/IP 二进制</td></tr><tr><td>BRNxxxxxxxxxxxxx_AT</td><td>Macintosh 的 PostScript® 服务</td></tr><tr><td>POSTSCRIPT_P1</td><td>PostScript® 服务(切换 PJL-兼容打印机到 PostScript® 模式)</td></tr></table>

"xxxxxxxxxxxx" 为您的打印机的 MAC 地址 ( 以太网地址 )。

# 设置 IP 地址的其他方法 ( 适用于高级用户和管理员 )

关于如何使用 BRAdmin Light 实用程序或网络基本管理 (网络浏览器 ) 配置您的网络设备，请参考第 13 页上的设置 IP 地址和子网掩码。

# 使用 DHCP 配置 IP 地址

动态主机配置协议 (DHCP) 是一种自动分配 IP 地址的机制。如果网络中有 DHCP 服务器，打印服务器将自动从 DHCP 服务器获取 IP 地址，并使用任意与 RFC 1001 和 1002 兼容的动态名称服务来注册名称。

![图片标题：介绍打印服务器通过DHCP自动获取IP地址及使用静态IP配置的方法。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/61d53c60f2562c72c122227d078518cdfe134427a2b8c1fba58c93f24e7e7324.jpg)

# 注释

如果您不想通过 DHCP、BOOTP 或 RARP 配置打印服务器，则必须将引导方式设置为静态，这样您的打印服务器便会获取一个静态 IP 地址，从而确保打印服务器不从任何其他系统获取 IP 地址。若要更改引导方式，请使用设备操作面板上的 Network (网络) 菜单、BRAdmin 应用程序或网络基本管理 (网络浏览器)。

# 使用 BOOTP 配置 IP 地址

BOOTP 可以代替 rarp ( 逆向地址解析协议 )，其优势在于可配置子网掩码和网关。若要使用 BOOTP 配置 IP地址，必须确认安装有 BOOTP 并已在您的主机上运行 (它将在主机的 /etc/services 文件中作为实时服务器出现；如需获取更多信息，请输入 manbootpd 或参考系统文件 )。 BOOTP 一般通过/etc/inetd.conf 文件启动，此时您可能需要删除文件中 bootp 项前的 "#" 才可启动。例如，/etc/inetd.conf 文件中典型的 bootp 项为：

#bootp dgram udp wait /usr/etc/bootpd bootpd -i

根据系统，此项可能被称为 “bootps” 而不是 “bootp”。

![BOOTP服务配置示例及启动方法说明，包括服务项名称、如何启用及配置文件编辑提示。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/5a1fe19bc210f0fca75ca645bb2649c4dea6c19d5b282d6ca7654f207109e774.jpg)

# 注释

只需使用编辑器删除 “#”，便可启动 BOOTP ( 如果没有 “#”，说明 BOOTP 已启动 )。然后编辑 BOOTP 配置文件 ( 一般为 /etc/bootptab) 并输入打印服务器的名称、网络类型 (1 为以太网 )、MAC 地址 ( 以太网地址 ) 以及 IP 地址、子网掩码和网关。但是这种操作的格式仍无统一标准，所以您必须参考您的系统文件，决定如何输入此类信息 ( 在 bootptab 文件中，许多 UNIX 系统也有模板例子，您可以将其作为参考 )。一些典型的 /etc/bootptab 例子包括：( 对于无线网络，下例中的 “BRN” 为 “BRW”。 )

BRN008077310107 1 00:80:77:31:01:07 192.189.207.3

和：

BRN008077310107:ht=ethernet:ha=008077310107:\ip=192.189.207.3:

如果在配置文件中未包括一个下载文件名，某些 BOOTP 主机软件将无法响应 BOOTP 的请求。在这种情况下，只需在主机中建立一个空文件并在配置文件中指定这个文件的名称和路径。

由于使用 RARP ( 逆向地址解析协议 )，打印服务器将在打印机电源接通时，从 BOOTP 服务器加载自己的IP 地址。

# 使用 RARP 配置 IP 地址

可以使用主机上的逆向地址解析协议 (RARP) 配置 Brother 打印服务器的 IP 地址。通过编辑 /etc/ethers文件 (如果文件不存在，您可以新建一个文件 ) 来完成，输入大致如下：

00:80:77:31:01:07 BRN008077310107 (BRW008077310107 适用于无线网络 )。

第一个输入的位置为打印服务器的 MAC 地址 ( 以太网地址 )，第二个输入的位置为打印服务器名称 ( 该名称必须与 /etc/hosts 文件中输入的名称相同 )。

如果后台逆向地址解析协议 (RARP daemon) 并未运行，请启动该程序 ( 根据系统的不同，命令也有所不同，如 rarpd、 rarpd -a、 in.rarpd -a 或其他命令；如需获取更多信息，请输入 man rarpd 或参考您的系统文件 )。确认后台逆向地址解析协议是否在 Berkeley UNIX based 系统中运行，输入以下命令：

```shell
ps -ax | grep -v grep | grep rarpd 
```

对于 AT&T UNIX-based 系统，输入：

```shell
ps -ef | grep -v grep | grep rarpd 
```

Brother 打印服务器将在打印机电源接通时，从后台逆向地址解析协议获取 IP 地址。

# 使用 APIPA 配置 IP 地址

本 Brother 打印服务器支持自动专用 IP 寻址 (APIPA) 协议。当 DHCP 服务器不可用时，使用 APIPA 和DHCP 的客户端自动配置一个 IP 地址和子网掩码。设备将在 169.254.1.0 至 169.254.254.255 范围内选择自己的 IP 地址。子网掩码将自动设置为 255.255.0.0，网关地址将设置为 0.0.0.0。

默认状态下， APIPA 协议为启用。如果您想禁用 APIPA 协议，请参考第 16页上的更改打印服务器设置。

如果 APIPA 协议为禁用，Brother 打印服务器的默认 IP 地址为 192.0.0.192。但是，您可以很容易地将此 IP地址更改为与您网络相匹配的 IP 地址。

# 使用 ARP 配置 IP 地址

即使您不能使用 BRAdmin 应用程序，并且您的网络不使用 DHCP 服务器，您也能使用 ARP (地址解析协议)命令。ARP 命令可以用于安装了 TCP/IP 协议的 Windows® 系统和 UNIX 系统。若要使用 ARP，在命令提示符中输入以下命令：

```txt
arp -s ipaddress ethernetaddress 
```

ethernetaddress 为打印服务器的 MAC 地址 ( 以太网地址 )， ipaddress 为打印服务器的 IP 地址。例如：

#  Windows® 系统

Windows® 系统要求在每个 MAC 地址 ( 以太网地址 ) 的数字之间使用短横 “-”。

```batch
arp -s 192.168.1.2 00-80-77-31-01-07 
```

#  UNIX/Linux 系统

通常情况下， UNIX 和 Linux 系统要求在 MAC 地址 ( 以太网地址 ) 的数字之间使用冒号 “:”。

```batch
arp -s 192.168.1.2 00:80:77:31:01:07 
```

![使用`arp -s`命令在Linux系统中静态绑定IP与MAC地址，需确保与打印服务器同网段。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/a194e8f590a2e14c03c2812b5d130647001f1f4c695182c1522bb468d8922bac.jpg)

# 注释

您必须与打印服务器处于相同的网段 ( 即：在打印服务器和操作系统之间不能有路由器 ) 才能使用 arp-s 命令。

如果有路由器，您可以使用 BOOTP 或本章所述的其他方式输入 IP 地址。如果管理员已经使用 BOOTP、DHCP 或 RARP 来配置系统，传递 IP 地址，那么您的 Brother 打印服务器可以从任何一个 IP 地址分配系统中接收 IP 地址。此时，您将不需要使用 ARP 命令。ARP 命令仅运行一次。出于安全考虑，一旦您使用了 ARP 命令成功配置 Brother 打印服务器的 IP 地址，您将不能使用其再次更改 IP 地址。打印服务器将忽略任何类似尝试。如果您需要再次更改 IP 地址，请使用网络基本管理 ( 网络浏览器 )、TELNET ( 使用 SETIP ADDRESS 命令 ) 或将打印服务器恢复到出厂默认设置 ( 这样才将允许您再次使用 ARP 命令 )。

若要配置打印服务器和确认连接，请输入以下命令：ping ipaddress。 ipaddress 为打印服务器的 IP地址。例如， ping 192.189.207.2。

# 使用 TELNET 控制台配置 IP 地址

您也可以使用 TELNET 命令更改 IP 地址。

TELNET 是一种更改设备 IP 地址的有效方法。但是一个有效的 IP 地址必须已编入打印服务器。

在系统提示的命令提示符中输入 TELNET ipaddress， ipaddress 为打印服务器的 IP 地址。连接时，按返回键或回车键取得 “#” 符号，输入密码 “access” ( 密码将不会在屏幕上显示 )。

提示要求输入用户名。请输入任意用户名。

你将看到 Local> 的提示符。输入 SET IP ADDRESS ipaddress，ipaddress 为您要配置到打印服务器的 IP 地址 ( 请与您的网络管理员一起检查可用的 IP 地址 )。例如：

```batch
Local> SET IP ADDRESS 192.168.1.3 
```

您现在需要通过输入 SET IP SUBNET subnet mask 设定子网掩码，subnet mask 为您想要配置到打印服务器的子网掩码 (请与您的网络管理员一起检查可用的子网掩码 )。例如：

```batch
Local> SET IP SUBNET 255.255.255.0 
```

如果您没有子网掩码，请使用以下默认的子网掩码：

A 类网络使用 255.0.0.0

B 类网络使用 255.255.0.0

C 类网络使用 255.255.255.0

在 IP 地址中最左侧的数字组能够识别您所处的网络类型。A 类网络组值范围从 1 到 127 ( 例如：13.27.7.1)，B 类网络组值从 128 到 191 ( 例如：128.10.1.30)， C 类网络组值从 192 到 255 ( 例如：192.168.1.4)。

如果您有网关 ( 路由器 )，请使用命令 SET IP ROUTER routeraddress 输入其地址， routeraddress为您想要分配到打印服务器的网关 IP 地址。例如：

```batch
Local> SET IP ROUTER 192.168.1.4 
```

输入 SET IP METHOD STATIC 设置 IP 访问配置方式为静态配置。

若要确认您是否正确输入 IP 信息，请输入 SHOW IP。

输入 EXIT 或 Ctrl-D ( 例如：按住 Ctrl 键并输入 “D”) 结束远程控制台会话。

# 使用 Brother Web BRAdmin 服务器软件对 IIS 进行 IP 地址的配置

Web BRAdmin 服务器软件用于管理局域网和无线网络中的 Brother 设备。通过在运行 IIS 1 的计算机上安装Web BRAdmin 服务器软件，管理员即可通过网络浏览器连接到 Web BRAdmin 服务器，然后与设备本身进行通信。不同于专为 Windows® 系统设计的 BRAdmin 专业版 3 实用程序，可以从任何带有支持 Java 的网络浏览器的客户端计算机上访问 Web BRAdmin 服务器软件。

请注意， Brother 产品随机光盘中不包含此软件。

请登录以下网站获取关于该软件的更多信息并下载该软件：http://solutions.brother.com/。

# 使用网络打印队列或共享时的安装

![Brother打印机软件下载及网络共享打印机安装指南，包括咨询管理员获取队列名、安装驱动等步骤。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/afa344f464307bb3fbd4267a5f29f5420fb3dde02ed62f71e2cc33189c4ae3a6.jpg)

# 注释

若要在您的网络中连入一台共享打印机，Brother 建议您在安装前向系统管理员咨询该打印机的队列或共享名称。

# 安装驱动程序并选择正确的打印机队列或共享名称

a 启动计算机。 ( 必须以管理员身份登录。 )配置前请关闭所有正在运行的应用程序。  
b 将随机光盘插入 CD-ROM 光驱中。将自动显示打开屏幕。选择打印机型号和语言。  
c 出现随机光盘主菜单。点击安装打印机驱动程序。  
d 点击网络电缆用户。

![安装打印机驱动程序步骤：插入随机光盘，选择型号和语言，点击安装，同意许可证协议。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/cf24f6d6ae2b2d646cb9ff16655da0f2e72209d4496b731b3e8aaf9e277d995b.jpg)

# 注释

当出现用户帐户控制屏幕时：

(Windows Vista®) 点击继续。

(Windows® 7) 点击是。

e 出现许可证协议窗口时，如果您同意此许可证协议，请点击是。

f 选择 网络共享打印机，然后点击下一步。

g 选择您的打印机队列，然后点击确定。

![安装网络共享打印机步骤：同意协议，选择网络共享打印机及队列，最后点击完成。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/3f721dcbbead03e5399d728ab531f0594c57ce41d5d23c03600ae9a5ea0e5e2a.jpg)

# 注释

如果您不确定网络中的打印机的位置和名称，请联系管理员。

h 点击完成。

![设置打印机选项：可选择是否设为默认打印机及启用状态监控器。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/da03fc95b4746864ddc4d210e333ff56284be8e6ea455a6ea1eb37f1f8a4e427.jpg)

# 注释

• 如您不想将打印机设置为默认打印机，请勿选中设为默认打印机。  
• 如果您想禁用状态监控器，请勿选中启用状态监控器。

![设置打印机选项：选择是否设为默认打印机及启用状态监控器。适用于Windows Vista® 和 Windows® 7。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/7700465df827278887a8a1962e621e5c6d482c97eba90aed59d2fe96e672225d.jpg)

# 设置完成。

# 使用网络服务时的安装

# ( 适用于 Windows Vista® 和 Windows® 7 用户 )

操作步骤可能会因操作系统的不同而有所不同。

![设置网络服务安装步骤（适用于Windows Vista®和Windows® 7），需先配置IP地址并确保设备在同一子网。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/bc0decfbcc2f32b4c7f3de46becde0d14349fee0fb79ad34ea0444c70db34678.jpg)

# 注释

• 执行此部分的操作前，您必须配置设备的 IP 地址。如果您尚未配置 IP 地址，请首先参考第13 页上的设置IP地址和子网掩码。  
• 验证主机和打印服务器处于同一子网中，或者路由器已正确配置以便在两设备之间传送数据。

点击 按钮，然后选择网络。

b 设备的网络服务名称将与打印机图标一起显示。右击您想安装的设备。

![验证网络设置后，选择并右击目标设备的网络服务名称以开始安装。](http://localhost:9000/knowledge-base-files/upload-images/hl3040网络说明书/42e4864134d63e30ff19a9e22b470131b2a5b399d32d1bf4bd7c0844ec09d9a6.jpg)

# 注释

Brother 设备的网络服务名称为本设备的型号名称和 MAC 地址 ( 以太网地址 ) ( 例如：Brother HL-XXXX[XXXXXXXXXXXX])。

c 点击安装。

d 出现用户帐户控制屏幕时，执行以下操作：

 具有管理员权限的用户：点击继续或是。  
 不具有管理员权限的用户：输入管理员密码并点击确定或是。

e 选择查找并安装驱动程序软件 ( 推荐 )。

f 插入 Brother 随机光盘。

选择不进行在线搜索，然后点击计算机上的浏览计算机以查找驱动程序软件 ( 高级 )。

h 选择 CD-ROM 光驱，然后选择 install\your language\PCL\32 1 文件夹。

1 对于 32 位 OS 用户，此处为 32 文件夹；对于 64 位 OS 用户，此处为 64 文件夹。

i 点击下一步开始安装。

# B 附录

# 打印服务器规格

有线以太网

<table><tr><td>网络节点名称</td><td>NC-6700h</td><td></td></tr><tr><td>局域网</td><td>您可以将您的设备联网以进行网络打印。</td><td></td></tr><tr><td>支持的操作系统</td><td> $Windows^{\textregistered}$  2000专业版、 $Windows^{\textregistered}$  XP、 $Windows^{\textregistered}$  XP专业版x64版本、Windows Vista®、 $Windows^{\textregistered}$  7,Windows Server®2003/2003 x64版本和Windows Server®2008/2008 R2Mac OS X 10.3.9或更高版本1</td><td></td></tr><tr><td rowspan="2">协议</td><td>IPv4:</td><td>ARP、RARP、BOOTP、DHCP、APIPA (Auto IP)、WINS/NetBIOS域名解析、DNS解析、mDNS、LLMNR应答器、LPR/LPD、自定义原始端口/端口/Port9100、IPP、IPPS、FTP服务器、SSL/TLS、POP优先于SMTP、SMTP-AUTH、APOP、TELNET服务器、SNMPv1、SNMPv2c、SNMPv3、HTTP/HTTPS服务器、TFTP客户端和服务器、SMTP客户端、ICMP、网络服务打印、LLTD应答器</td></tr><tr><td> $IPv6^{2}$ :</td><td>(默认状态下关闭)NDP、RA、DNS解析、mDNS、LLMNR应答器、LPR/LPD、自定义原始端口/端口9100、IPP、IPPS、FTP服务器、SSL/TLS、POP优先于SMTP、SMTP-AUTH、APOP、TELNET服务器、SNMPv1、SNMPv2c、SNMPv3、HTTP/HTTPS服务器、TFTP客户端和服务器、SMTP客户端、ICMPv6、网络服务打印、LLTD应答器</td></tr><tr><td>网络类型</td><td colspan="2">以太网10/100 BASE-TX自动协商(有线局域网)</td></tr><tr><td rowspan="5">管理实用程序</td><td> $BRAdmin Light ^{3}$ </td><td></td></tr><tr><td> $BRAdmin$ 专业版 $3^{4}$ </td><td></td></tr><tr><td> $Web$   $BRAdmin ^{45}$ </td><td></td></tr><tr><td> $BRPrint$   $Auditor ^{46}$ </td><td></td></tr><tr><td colspan="2">网络基本管理(网络浏览器)</td></tr></table>

1 关于最新的驱动程序更新，请访问以下网站：http://solutions.brother.com/ 获取更多信息。  
2 如果您想使用 IPv6 协议，请访问以下网站：http://solutions.brother.com/ 获取更多信息。  
3 如果您需要更高级的打印机管理，请使用最新版本的 Brother BRAdmin 专业版 3 实用程序，可登录以下网站：http://solutions.brother.com/ 下载。  
4 请登录以下网站 Web BRAdmin、 BRAdmin 专业版 3 和 BRPrint Auditor：http://solutions.brother.com/ 下载，这些软件仅适用于 Windows®。  
5 带有支持 Java 的网络浏览器的客户端计算机。  
6 在通过 USB 连接到客户端计算机的设备上使用 BRAdmin 专业版 3 或 Web BRAdmin 时可用。

无线网络 ( 适用于 HL-3070CW)

<table><tr><td>网卡型号名称</td><td>NC-7500w</td><td></td></tr><tr><td>局域网</td><td>您可以将您的设备联网以进行网络打印。</td><td></td></tr><tr><td rowspan="2">支持的操作系统</td><td>Windows®2000专业版、Windows®XP、Windows®XP专业版x64版本、Windows Vista®、Windows®7, Windows Server®2003/2003 x64版本和Windows Server®2008/2008 R2</td><td></td></tr><tr><td>Mac OS X 10.3.9或更高版本1</td><td></td></tr><tr><td rowspan="2">协议</td><td>IPv4:</td><td>ARP、RARP、BOOTP、DHCP、APIPA (Auto IP)、WINS/NetBIOS域名解析、DNS解析、mDNS、LLMNR应答器、LPR/LPD、自定义原始端口/端口9100、IPP、IPPS、FTP服务器、SSL/TLS、POP优先于SMTP、SMTP-AUTH、APOP、TELNET服务器、SNMPv1、SNMPv2c、SNMPv3、HTTP/HTTPS服务器、TFTP客户端和服务器、SMTP客户端、ICMP、网络服务打印、LLTD应答器</td></tr><tr><td>IPv62:</td><td>(默认状态下关闭)NDP、RA、DNS解析、mDNS、LLMNR应答器、LPR/LPD、自定义原始端口/端口9100、IPP、IPPS、FTP服务器、SSL/TLS、POP优先于SMTP、SMTP-AUTH、APOP、TELNET服务器、SNMPv1、SNMPv2c、SNMPv3、HTTP/HTTPS服务器、TFTP客户端和服务器、SMTP客户端、ICMPv6、网络服务打印、LLTD应答器</td></tr><tr><td>网络类型</td><td>IEEE 802.11 b/g(无线局域网)</td><td></td></tr><tr><td rowspan="5">管理实用程序</td><td>BRAdmin Light3</td><td></td></tr><tr><td>BRAdmin专业版34</td><td></td></tr><tr><td>Web BRAdmin45</td><td></td></tr><tr><td>BRPrint Auditor46</td><td></td></tr><tr><td>网络基本管理(网络浏览器)</td><td></td></tr><tr><td>频率</td><td>2412-2472 MHz</td><td></td></tr><tr><td rowspan="3">RF信道</td><td>美国/加拿大</td><td>1-11</td></tr><tr><td>日本</td><td>802.11b:1-14, 802.11g:1-13</td></tr><tr><td>其他</td><td>1-13</td></tr><tr><td>通信模式</td><td>基础架构、Ad-hoc(仅802.11b)</td><td></td></tr><tr><td rowspan="2">数据率</td><td>802.11b</td><td>11/5.5/2/1 Mbps</td></tr><tr><td>802.11g</td><td>54/48/36/24/18/12/11/9/6/5.5/2/1 Mbps</td></tr><tr><td rowspan="2">连接距离</td><td>最低的数据率时为70 m (233 ft.)</td><td></td></tr><tr><td>(距离率因环境和其他设备位置的不同而不同。)</td><td></td></tr><tr><td>网络安全</td><td>128 (104)/64 (40)位 WEP、WPA-PSK (TKIP/AES)、WPA2-PSK (AES)、LEAP (CKIP)、EAP-FAST (TKIP/AES)</td><td></td></tr><tr><td>设置支持的实用程序</td><td>SecureEasySetup、Wi-Fi Protected Setup、AOSSTM</td><td></td></tr></table>

1 关于最新的驱动程序更新，请访问以下网站：http://solutions.brother.com/ 下载。

2 如果您想使用 IPv6 协议，请访问以下网站：http://solutions.brother.com/ 获取更多信息。  
3 如果您需要更高级的打印机管理，请使用最新版本的 Brother BRAdmin 专业版 3 实用程序，可访问以下网站：http://solutions.brother.com/ 下载。  
4 请访问以下网站：http://solutions.brother.com/ 下载 Web BRAdmin、 BRAdmin 专业版 3 和 BRPrint Auditor，这些软件仅适用于 Windows®。  
5 带有支持 Java 的网络浏览器的客户端计算机。  
6 在通过 USB 连接到客户端计算机的设备上使用 BRAdmin 专业版 3 或 Web BRAdmin 时可用。

# 功能表和出厂默认设置

出厂默认设置以粗体显示并带有 “\*” 号。

(HL-3040CN) 

<table><tr><td>一级菜单</td><td>二级菜单</td><td>三级菜单</td><td>选项</td></tr><tr><td rowspan="9">Network(网络)</td><td rowspan="7">TCP/IP</td><td>Boot Method(引导方式)</td><td>Auto*(自动)、Static(静态)、RARP、BOOTP、DHCP</td></tr><tr><td>IP Address(IP地址)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>Subnet Mask(子网掩码)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>Gateway(网关)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>IP Boot Tries(尝试IP启动)</td><td>0~327673*</td></tr><tr><td>APIPA</td><td>On*(开)、Off(关)</td></tr><tr><td>IPv6</td><td>On(开)、Off*(关)</td></tr><tr><td>Ethernet</td><td>-</td><td>Auto*(自动)、100B-FD、100B-HD、10B-FD、10B-HD</td></tr><tr><td>Factory Reset(出厂设置)</td><td>-</td><td>Restart Printer?(重启打印机?)</td></tr></table>

(HL-3070CW) 

<table><tr><td>一级菜单</td><td>二级菜单</td><td>三级菜单</td><td>四级菜单</td><td>选项</td></tr><tr><td rowspan="14">Network(网络)</td><td rowspan="10">Wired LAN(有线局域网)</td><td rowspan="7">TCP/IP</td><td>Boot Method(引导方式)</td><td>Auto*(自动)、Static(静态)、RARP、BOOTP、DHCP</td></tr><tr><td>IP Address(IP地址)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>Subnet Mask(子网掩码)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>Gateway(网关)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>IP Boot Tries(尝试IP启动)</td><td>0~327673*</td></tr><tr><td>APIPA</td><td>On*(开)、Off(关)</td></tr><tr><td>IPv6</td><td>On(开)、Off*(关)</td></tr><tr><td>Ethernet</td><td>-</td><td>Auto*(自动)、100B-FD、100B-HD、10B-FD、10B-HD</td></tr><tr><td>Set to Default(设为默认值)</td><td>-</td><td>OK?(确定?)</td></tr><tr><td>Wired Enable(启用有线网络)</td><td>-</td><td>On*(开)、Off(关)</td></tr><tr><td rowspan="4">WLAN(无线局域网)</td><td rowspan="4">TCP/IP</td><td>Boot Method(引导方式)</td><td>Auto*(自动)、Static(静态)、RARP、BOOTP、DHCP</td></tr><tr><td>IP Address(IP地址)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-0O0].[000-000]*</td></tr><tr><td>Subnet Mask(子网掩码)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td>Gateway(网上关)</td><td>[000-255].[000-255].[000-255].[000-255][000-000].[000-000].[000-000].[000-000]*</td></tr><tr><td rowspan="14">Network(网络)</td><td rowspan="13">WLAN(无线局域网)</td><td rowspan="3">TCP/IP</td><td>IP Boot Tries(尝试IP启动)</td><td>0~327673*</td></tr><tr><td>APIPA</td><td>On*(开)、Off(关)</td></tr><tr><td>IPv6</td><td>On(开)、Off*(关)</td></tr><tr><td>SES/WPS/AOSS</td><td>-</td><td>请参考第6章的3使用操作面板上的SES/WPS或AOSS进行的无线配置(适用于HL-3070CW)。</td></tr><tr><td>WPS w/PIN Code(有PIN密码的WPS)</td><td>-</td><td>请参考第7章的使用Wi-Fi Protected Setup的PIN方式的无线配置(适用于HL-3070CW)。</td></tr><tr><td rowspan="6">WLAN Status(无线网络状态)</td><td>Status(状态)</td><td>请参考第63页上的状态。</td></tr><tr><td>Signal(信号)</td><td>请参考第64页上的信号。</td></tr><tr><td>Channel(信道)</td><td>请参考第64页上的信道。</td></tr><tr><td>Speed(速度)</td><td>请参考第65页上的速度。</td></tr><tr><td>SSID</td><td>请参考第65页上的SSID。</td></tr><tr><td>Comm.Mode(通信模式)</td><td>请参考第66页上的通信模式。</td></tr><tr><td>Set to Default(设为默认值)</td><td>-</td><td>OK?(确定?)</td></tr><tr><td>WLAN Enable(启用无线网络)</td><td>-</td><td>On(开)、Off*(关)</td></tr><tr><td>Factory Reset(出厂设置)</td><td>-</td><td>-</td><td>Restart Printer?(重启打印机?)</td></tr></table>

# C

# 索引

# A

AES . ... 20

AOSS ..25, 39

APIPA . 7, 59, 130

APOP .. 91

ARP .. 131

安全协议 .. 91

# B

BINARY\_P1 .. 128

BOOTP ... 7, 54, 129

BRAdmin Light .... 1, 2, 13, 16

BRAdmin 专业版 3 .... 1, 2, 16, 96

BRNxxxxxxxxxxxx . 128

BRNxxxxxxxxxxxx\_AT .. 128

BRPrint Auditor . 3

# C

CA ...90, 103

CKIP . ... 20

CSR ... 90

操作面板 .. 17

操作系统

尝试 IP 启动 ... 58

出厂默认设置 ... 67

# D

DHCP .... 7, 54, 128

DNS ....7, 92, 93, 101, 103

打印服务器设置 .. 16

对等 4

# E

EAP-FAST ... 20

# F

防火墙 ..121, 124

服务 . 128

# G

公共键加密系统 ... 90

共享键加密系统 .. 90

共享密钥 . 19

规格 . .. 136

# H

HTTP 9

HTTPS . 93

恢复出厂设置 .. 61

# J

基础架构模式 .... 6, 22, 23

机密键 .. 103

IP 地址 . 10

IPP ....8, 81

IPPS . ....91, 100

IPv6 . ......9, 60

加密 . 19

# K

开放系统 .. .. 19

# L

LEAP .. 19

LLMNR 8

LLTD 9

LPR/LPD 8

# M

MAC 地址 .. 68

mDNS 8

密码 ... 81

# P

PCL\_P1 .. 128

PIN 方式 . ....26, 43

Ping . ..124, 125

POP 优先于 SMTP ....91, 101

Port9100 8

POSTSCRIPT\_P1 .. 128

# Q

驱动程序配置向导 ....1, 69

# R

RARP .. 7, 54, 130

RFC 1001 . .. 128

# S

SecureEasySetup ...25, 39

SMTP 客户端 8

SMTP-AUTH ...91, 101

SNMP . 8

SNMPv3 .... 91

SSID ( 服务区标识符 ) ... .. 19

SSL/TLS . ..91, 103

商标 .

设为默认值 ... 61

数字签名 ... 90

# T

TCP/IP ....7, 53

TCP/IP 打印 .. 77

Telnet ...8, 132

TEXT\_P1 ... 128

TKIP . .. 20

# W

Web BRAdmin 3

WEP . .... 20

Wi-Fi Protected Setup ... 25, 39, 43

WPA2-PSK .. 19

WPA-PSK .. 19

网关 .. 57

网络打印 ..77, 81

网络服务 8

网络服务器 (HTTP) 9

网络服务器 (HTTPS) ... 91

网络共享打印 5

网络基本管理 ( 网络浏览器 ) .. . 3, 92, 93

网络浏览器 (HTTP) .. 17

网络密钥 ... 21

网络配置页 . 68

无线网络 ....6, 18

# X

协议 . ....7, 92

信道 . . 19

# Y

验证 .. 19

以太网 ... 61

因特网打印

# Z

证书 ...90, 103

状态监视器

自定义原始端口 8

子网掩码 ..11, 56