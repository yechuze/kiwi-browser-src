# 猕猴桃浏览器

[![自动构建apk](https://github.com/kiwibrowser/src/workflows/automatic%20build%20of%20apk/badge.svg)
## 概述

[Kiwi Browser](https://kiwibrowser.com/)是一款完全开源的安卓网络浏览器。

Kiwi 基于 Chromium。轻松切换到 Kiwi，无需费力学习新界面或打破现有浏览习惯。

除其他功能外，Kiwi 浏览器还支持：

- 夜间模式（Chromium 之外的另一种实现）
- 支持 Chrome 扩展
- 底部地址栏 它还包括性能改进（瓷砖的部分光栅化等）

该浏览器的许可与 Chromium 相同，这意味着您可以创建浏览器的衍生产品。

确保正确地将代码归因于此存储库（不要只替换为您的姓名）

## 目录

- [时间线](#timeline)
- [贡献](#contributing)
- [修改](#modifying)
- [建筑](#building)
  - [获取源代码和环境](#getting-the-source-code-and-environment)
  - [设置依赖项](#setting-up-dependencies)
  - [准备签名密钥](#preparing-a-signing-key)
  - [配置构建类型和平台](#configuring-the-build-type-and-platform)
  - [准备第一个构建](#preparing-the-first-build)
  - [编译 Kiwi 浏览器](#compiling-kiwi-browser)
  - [调查崩溃](#investigating-crashes)
  - [远程调试](#remote-debugging)
  - [优化二进制大小](#optimizing-binary-size)
- [路线图](#roadmap)
- [其他帮助](#additional-help)

## 时间线

- 2018 年 4 月 15 日 - 首次发布 Kiwi 浏览器。
- 2019 年 4 月 15 日 - Kiwi 浏览器获得对 Chrome 扩展的支持。
- 2020 年 4 月 17 日 - Kiwi 浏览器完全开源。

此代码是最新的，并且与 Play 商店上的构建相匹配。

新版本是从开源版本直接到[Play Store](https://play.google.com/store/apps/details?id=com.kiwibrowser.browser)完成的。

此存储库中有数千小时的工作，并且更改了数千个文件。

## 贡献

欢迎和鼓励贡献。

如果您希望将您的代码集成到 Kiwi 中，请打开合并请求，我（和/或社区成员）可以与您一起审查代码并将其推送到 Play 商店。

## 修改

如果您创建自己的浏览器或模组，请确保更改浏览器名称和图标以及翻译字符串（在 all 、 all和 all文件`chrome/android/java/res_chromium/values/channel_constants.xml`中搜索和替换 Kiwi ）。更换应用程序图标时，请确保在各自的文件夹（mdpi、hdpi 等）中添加新图标文件，并更新 AndroidManifest.xml。`*.xtb``*.grd``*.grdp``chrome/android/java/res/mipmap`

## 构建

参考构建机器使用的是 Ubuntu 19.04（也使用 Ubuntu 18.04 和 Ubuntu 19.10 进行了测试）。

最低系统要求为 2 个 vCPU、7.5 GB 内存。

您可以使用虚拟机、AWS VM 或 Google Cloud VM。

### 获取源代码和环境

要构建 Kiwi Browser，您可以直接克隆存储库，因为我们已经打包了所有依赖项：

在〜（您的主目录）中运行：

```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
```

并编辑文件 ~/.bashrc 在最后添加

```
export PATH= $HOME /depot_tools: $PATH
```

通过运行验证更改：

```
source 〜/ .bashrc
```

这将使您可以访问一个名为 gclient 的实用程序（如“Google 客户端”）

创建一个名为 ~/chromium/ 的目录，并在 ~/chromium/ 中运行：

```
git clone https://github.com/kiwibrowser/dependencies.git .cipd
cp ~ /chromium/.cipd/.gclient ~ /chromium/
cp ~ /chromium/.cipd/.gclient_entries ~ /chromium/
git clone https://github.com/kiwibrowser/src.git
```

在这个阶段，在 ~/chromium/ 中，您将拥有 .cipd 文件夹，以及一个名为 src 的包含 Kiwi 浏览器源代码的文件夹。

### 设置依赖项

为了能够构建 Kiwi 浏览器，您需要 python 和 OpenJDK（OpenJDK 为 Android 创建 Java 绑定）：

```
sudo apt-get update
sudo apt-get install python openjdk-8-jdk-headless libncurses5
```

我们要确保使用 Java 1.8，以免出现编译错误（lint 和容易出错）：

```
sudo update-java-alternatives --set java-1.8.0-openjdk-amd64
```

然后在 ~/chromium/src 中运行以下命令：

```
bash install-build-deps.sh --no-chromeos-fonts
build/linux/sysroot_scripts/install-sysroot.py --arch=i386
build/linux/sysroot_scripts/install-sysroot.py --arch=amd64
```

这些命令将使用 apt-get 安装所有必要的系统包并收集最小的构建文件系统。

### 准备签名密钥

Android 上的 APK（应用程序包）需要开发者签名才能分发。

要生成密钥：

```
keytool -genkey -v -keystore ~ /chromium/keystore.jks -alias production -keyalg RSA -keysize 2048 -validity 10000 -storepass HERE_YOUR_ANDROID_KEYSTORE_PASSWORD -keypass HERE_YOUR_ANDROID_KEYSTORE_PASSWORD
```

### 配置构建类型和平台

run：

```
mkdir -p ~ /chromium/src/out/android_arm
```

在 ~/chromium/src/out/android_arm/ 中创建一个名为 args.gn 的文件，其中包含以下内容：

```bash
target_os = "android"
target_cpu = "arm" # <---- can be arm, arm64, x86 or x64
is_debug = false
is_java_debug = false

android_channel = "stable"
is_official_build = true
is_component_build = false
is_chrome_branded = false
is_clang = true
symbol_level = 1
use_unofficial_version_number = false
android_default_version_code = "158"
android_keystore_name = "production"
android_keystore_password = "HERE_YOUR_ANDROID_KEYSTORE_PASSWORD"
android_keystore_path = "../../../keystore.jks"
android_default_version_name = "Quadea"
fieldtrial_testing_like_official_build = true
icu_use_data_file = false
enable_iterator_debugging = false

google_api_key = "KIWIBROWSER"
google_default_client_id = "42.apps.kiwibrowser.com"
google_default_client_secret = "KIWIBROWSER_NOT_SO_SECRET"
use_official_google_api_keys = true

ffmpeg_branding = "Chrome"
proprietary_codecs = true
enable_hevc_demuxing = true
enable_nacl = false
enable_wifi_display = false
enable_widevine = false
enable_google_now = true
enable_ac3_eac3_audio_demuxing = true
enable_iterator_debugging = false
enable_mse_mpeg2ts_stream_parser = true
enable_remoting = false
rtc_use_h264 = false
rtc_use_lto = false
use_openh264 = false

v8_use_external_startup_data = true
update_android_aar_prebuilts = true

use_thin_lto = true

enable_extensions = true
enable_plugins = true
```

您可以将 Android 密钥库密码和 Android 密钥库密钥路径替换为您的 Android 密钥库的数据（或者您可以生成一个新密钥）。

### 准备第一个构建

要从 ~/chromium/src 准备初始设置运行：

```
gclient runhooks
```

然后在 ~/chromium/src 中生成构建文件：

```
gn gen out/android_arm
```

或者，您可以使用：gn args out/android_arm

### 编译 Kiwi 浏览器

要编译，请使用以下命令：

```
ninja -C out/android_arm chrome_public_apk
```

您将在 ~/chromium/src/out/android_arm/apks/ChromePublic.apk 中获得输出 APK

然后您可以在手机上运行 APK。

### 调查崩溃

您需要有崩溃版本的符号，可以使用以下方法生成符号：

```
components/crash/content/tools/generate_breakpad_symbols.py --build-dir=out/lnx64 --symbols-dir=/tmp/my_symbols/ --binary=out/android_arm/lib.unstripped/libchrome.so --clear --verbose
```

如果您有来自 logcat 的崩溃信息：

```
out/lnx64/microdump_stackwalk -s /tmp/dump.dmp /tmp/my_symbols/
```

如果您在墓碑中有崩溃信息：

```
./third_party/android_ndk/ndk-stack -sym out/android_x86/lib.unstripped -dump tombstone
```

### 远程调试

您可以使用 Google Chrome 使用 devtools 控制台进行调试。

如果 devtools 控制台不起作用（错误 404），解决方案是使用 chrome://inspect（检查后备）或在 build/util/LASTCHANGE 中更改 SHA1

```
LASTCHANGE=8920e690dd011895672947112477d10d5c8afb09-refs/branch-heads/3497@{#948}
```

并使用以下命令确认更改：

```
rm out/android_arm/gen/components/version_info/version_info_values.h out/android_x86/gen/components/version_info/version_info_values.h out/android_arm/gen/build/util/webkit_version.h out/android_x86/gen/build/util/webkit_version.h out/android_arm/gen/chrome/common/chrome_version.h out/android_x86/gen/chrome/common/chrome_version.h
```

### 优化二进制大小

如果要优化最终 APK，可以使用以下命令查看每个单独组件的大小：

```
./tools/binary_size/supersize archive chrome.size --apk-file out/android_arm/apks/ChromePublic.apk -v
./tools/binary_size/supersize html_report chrome.size --report-dir size-report -v
```

## 预编译的二进制文件

[![img](https://camo.githubusercontent.com/59c5c810fc8363f8488c3a36fc78f89990d13e99/68747470733a2f2f706c61792e676f6f676c652e636f6d2f696e746c2f656e5f75732f6261646765732f696d616765732f67656e657269632f656e5f62616467655f7765625f67656e657269632e706e67)](https://play.google.com/store/apps/details?id=com.kiwibrowser.browser)



## 商业模式

使用 Kiwi 浏览器完成的每次搜索，搜索引擎都会为该浏览器付费。

根据搜索引擎的选择，请求可能会通过 Kiwibrowser / Kiwisearchservices 服务器。这是为了向我们的搜索合作伙伴开具发票并提供替代搜索结果（例如，刘海又名“快捷方式”）。

在某些国家/地区，浏览器会在主页上显示赞助瓷砖或新闻。

不会收集用户数据（浏览、导航、密码、帐户），因为我们没有兴趣知道您在浏览器中所做的事情。我们的主要目标是说服您使用搜索引擎合作伙伴，该搜索引擎可以赚钱/建立新的合作伙伴关系并与我们分享收入。

## 路线图

- 在 2020 年，该项目的目标是进行维护修复和安全更新。

如果您希望包含到 Kiwi 中的问题或错误，请打开指向相关 Chromium 错误或提交的问题票。准确地说，Chromium 有成千上万的变化。

- 在 2021 年期间，Kiwi Browser 将切换到一个名为 Kiwi Browser Next 的新分支，该分支具有相当自动化的 Chromium 变基系统。

## 其他帮助

[您可以在我们的 Discord 服务器中寻求额外帮助，或](https://play.google.com/store/apps/details?id=com.kiwibrowser.browser)[提交问题](https://github.com/kiwibrowser/src/issues)。

[![img](https://camo.githubusercontent.com/25c4223a3586b2138655b499bec582c88bae354eddd40290f3fa5a04b3ab62a1/68747470733a2f2f646973636f72646170702e636f6d2f6173736574732f65343932333539346536393461323135343261343839343731656366666135302e737667)](https://discord.gg/XyMppQq)

和猕猴桃一起玩！

阿尔诺。
