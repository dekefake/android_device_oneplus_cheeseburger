# Copyright (C) 2016 Paranoid Android
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# Set the firmware path in the environment
target_firmware_path := $(ANDROID_BUILD_TOP)/device/oneplus/oneplus5-images

# Logo.bin
$(call add-firmware-file,$(target_firmware_path)/logo.bin)

# Firmware images
$(call add-firmware-file,$(target_firmware_path)/abl.elf)
$(call add-firmware-file,$(target_firmware_path)/adspso.bin)
$(call add-firmware-file,$(target_firmware_path)/BTFM.bin)
$(call add-firmware-file,$(target_firmware_path)/cmnlib64.mbn)
$(call add-firmware-file,$(target_firmware_path)/cmnlib.mbn)
$(call add-firmware-file,$(target_firmware_path)/devcfg.mbn)
$(call add-firmware-file,$(target_firmware_path)/hyp.mbn)
$(call add-firmware-file,$(target_firmware_path)/keymaster.mbn)
$(call add-firmware-file,$(target_firmware_path)/NON-HLOS.bin)
$(call add-firmware-file,$(target_firmware_path)/pmic.elf)
$(call add-firmware-file,$(target_firmware_path)/rpm.mbn)
$(call add-firmware-file,$(target_firmware_path)/static_nvbk.bin)
$(call add-firmware-file,$(target_firmware_path)/tz.mbn)
$(call add-firmware-file,$(target_firmware_path)/xbl.elf)

# Unset local variable
target_firmware_path :=
