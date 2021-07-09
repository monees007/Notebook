

Overview

17 March 2021

08:40 PM

Android 10 or higher modularizes some Android system

components and enables them to be updated outside of the

normal Android release cycle. End-user devices can receive

updates to these modularized system components from the

Google Play Store infrastructure or through a partner-provided

over-the-air (OTA) mechanism.

From <<https://source.android.com/devices/architecture/modular-system>>

About modular system components

Modular system components enable Google and Android

partners to distribute updates broadly, quickly, and seamlessly

to end-user devices in a nonintrusive manner. For example, the

combination of media codec fragmentation and critical bugs

can dramatically slow app adoption and user engagement.

Frequent updates to media-related modules can reduce codec

fragmentation to make media app behavior more consistent

across different Android devices and fix critical bugs to build

user trust.

From <<https://source.android.com/devices/architecture/modular-system>>

Architecture

Android 10 or higher converts selected system components

into modules, some of which use the [APEX](https://source.android.com/devices/tech/ota/apex)[ ](https://source.android.com/devices/tech/ota/apex)[container](https://source.android.com/devices/tech/ota/apex)[ ](https://source.android.com/devices/tech/ota/apex)[format](https://source.android.com/devices/tech/ota/apex)

(introduced in Android 10) and some of which use the APK

format. The modular architecture enables system components

to be updated with critical bug fixes and other improvements as

needed, without affecting lower-level vendor implementations

or higher-level apps and services.





Figure 1. Modularized system components

Module updates don't introduce new APIs. They use only the

SDK and System APIs guaranteed by the [Compatibility](https://source.android.com/compatibility/tests)[ ](https://source.android.com/compatibility/tests)[Test](https://source.android.com/compatibility/tests)

[Suite](https://source.android.com/compatibility/tests)[ ](https://source.android.com/compatibility/tests)[(CTS)](https://source.android.com/compatibility/tests), communicate only with each other, and use only

stable C API or [stable](https://source.android.com/devices/bootloader/stable-aidl)[ ](https://source.android.com/devices/bootloader/stable-aidl)[AIDL](https://source.android.com/devices/bootloader/stable-aidl)[ ](https://source.android.com/devices/bootloader/stable-aidl)[interfaces](https://source.android.com/devices/bootloader/stable-aidl).

Updated modular system components can be packaged

together and pushed to end-user devices, either by Google

(using the Google Play Store infrastructure) or by the Android

partner (using a partner-provided OTA mechanism). The

module package installs (and rolls back) atomically, meaning

all modules that need to be updated are updated or none are.

For example, if a module that needs to be updated can't be

updated for any reason, the device doesn't install any of the

modules in the package.

Available modules

Android includes the following modules.

Module name

[adbd](https://source.android.com/devices/architecture/modular-system/adbd)

Package name

Type

Release

introduced

com.google.android. APEX

adbd

Android 11

Android 10

Android 10

Android 11

Android 10

Android 10

[Runtime](https://source.android.com/devices/architecture/modular-system/runtime)

com.android.runtim APEX

e.release.apex

[Captive](https://source.android.com/devices/architecture/modular-system/networking)[ ](https://source.android.com/devices/architecture/modular-system/networking)[Portal](https://source.android.com/devices/architecture/modular-system/networking)

[Login](https://source.android.com/devices/architecture/modular-system/networking)

com.android.captive APK

portallogin

[CellBroadcast](https://source.android.com/devices/architecture/modular-system/cellbroadcast)

com.google.android. APEX

cellbroadcast

[Conscrypt](https://source.android.com/devices/architecture/modular-system/conscrypt)

com.android.conscr APEX

ypt

[DNS](https://source.android.com/devices/architecture/modular-system/dns-resolver)[ ](https://source.android.com/devices/architecture/modular-system/dns-resolver)[Resolver](https://source.android.com/devices/architecture/modular-system/dns-resolver)

com.android.resolv APEX





[DocumentsUI](https://source.android.com/devices/architecture/modular-system/documentsui)

[ExtServices](https://source.android.com/devices/architecture/modular-system/extservices)

com.android.docum APK

entsui

Android 10

Android 10

com.android.ext.ser APK

vices

(Android

\10)

APEX

(Android

\11)

[IPsec/IKEv2](https://source.android.com/devices/architecture/modular-system/ipsec)

[Library](https://source.android.com/devices/architecture/modular-system/ipsec)

com.google.android. APEX

ipsec

Android 11

Android 10

[Media](https://source.android.com/devices/architecture/modular-system/media)[ ](https://source.android.com/devices/architecture/modular-system/media)[Codecs](https://source.android.com/devices/architecture/modular-system/media)

com.android.media. APEX

swcodec

[Media](https://source.android.com/devices/architecture/modular-system/media)

com.android.media APEX

Android 10

(extractors,

MediaSession API)

Android 11

(MediaParser API)

[MediaProvider](https://source.android.com/devices/architecture/modular-system/media)

com.google.android. APEX

mediaprovider

Android 11

Android 10

Android 10

[ModuleMetadata](https://source.android.com/devices/architecture/modular-system/metadata)[ ](https://source.android.com/devices/architecture/modular-system/metadata)com.android.module APK

metadata

[Network](https://source.android.com/devices/architecture/modular-system/networking)[ ](https://source.android.com/devices/architecture/modular-system/networking)[Stack](https://source.android.com/devices/architecture/modular-system/networking)

[Permission](https://source.android.com/devices/architecture/modular-system/networking)

[Configuration](https://source.android.com/devices/architecture/modular-system/networking)

com.android.networ APK

kstack.permissionco

nfig

[Network](https://source.android.com/devices/architecture/modular-system/networking)

[Components](https://source.android.com/devices/architecture/modular-system/networking)

com.android.networ APK

kstack

Android 10

Android 11

Android 10

[NNAPI](https://source.android.com/devices/architecture/modular-system/nnapi)[ ](https://source.android.com/devices/architecture/modular-system/nnapi)[Runtime](https://source.android.com/devices/architecture/modular-system/nnapi)

com.google.android. APK

neuralnetworks

[PermissionControl](https://source.android.com/devices/architecture/modular-system/permissioncontroller)[ ](https://source.android.com/devices/architecture/modular-system/permissioncontroller)com.android.permis APK

[ler](https://source.android.com/devices/architecture/modular-system/permissioncontroller)

sioncontroller

[SDK](https://source.android.com/devices/architecture/modular-system/sdk-extension)[ ](https://source.android.com/devices/architecture/modular-system/sdk-extension)[Extensions](https://source.android.com/devices/architecture/modular-system/sdk-extension)

[Statsd](https://source.android.com/devices/architecture/modular-system/statsd)

com.android.sdkext APEX

Android 11

Android 11

com.google.android. APEX

os.statsd

[Telemetry](https://source.android.com/devices/architecture/modular-system/telemetry)[ ](https://source.android.com/devices/architecture/modular-system/telemetry)[Train](https://source.android.com/devices/architecture/modular-system/telemetry)

[Version](https://source.android.com/devices/architecture/modular-system/telemetry)[ ](https://source.android.com/devices/architecture/modular-system/telemetry)[Package](https://source.android.com/devices/architecture/modular-system/telemetry)[ ](https://source.android.com/devices/architecture/modular-system/telemetry)e.telemetry

com.google.mainlin APEX

Android 11

Android 11

[Tethering](https://source.android.com/devices/architecture/modular-system/tethering)

com.google.android. APK

tethering

[Time](https://source.android.com/devices/architecture/modular-system/timezone)[ ](https://source.android.com/devices/architecture/modular-system/timezone)[Zone](https://source.android.com/devices/architecture/modular-system/timezone)[ ](https://source.android.com/devices/architecture/modular-system/timezone)[Data](https://source.android.com/devices/architecture/modular-system/timezone)

[Wi-Fi](https://source.android.com/devices/architecture/modular-system/wifi)

com.android.tzdata APEX

Android 10

Android 11

com.google.android. APEX

wifi.apex

From <<https://source.android.com/devices/architecture/modular-system>>





Runtime

17 March 2021

08:49 PM


