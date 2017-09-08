# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017 The LineageOS Project
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

import hashlib
import common
import re

def FullOTA_Assertions(info):
  AddModemAssertion(info)
  return

def IncrementalOTA_Assertions(info):
  AddModemAssertion(info)
  return

def AddModemAssertion(info):
  android_info = info.input_zip.read("OTA/android-info.txt")
  m = re.search(r'require\s+version-modem\s*=\s*(.+)', android_info)
  if m:
    version = m.group(1).rstrip()
    if len(version) and '*' not in version:
      cmd = 'assert(cheeseburger.verify_modem("' + version + '") == "1");'
      info.script.AppendExtra(cmd)
  return

def InstallImage(img_name, img_file, partition, info):
  common.ZipWriteStr(info.output_zip, "firmware/" + img_name, img_file)
  info.script.AppendExtra(('package_extract_file("' + "firmware/" + img_name + '", "/dev/block/bootdevice/by-name/' + partition + '");'))

image_partitions = {
   'cmnlib64.mbn' : 'cmnlib64',
   'cmnlib.mbn' : 'cmnlib',
   'hyp.mbn' : 'hyp',
   'pmic.elf' : 'pmic',
   'tz.mbn' : 'tz',
   'abl.elf' : 'abl',
   'devcfg.mbn' : 'devcfg',
   'keymaster.mbn' : 'keymaster',
   'xbl.elf' : 'xbl',
   'rpm.mbn' : 'rpm',
   'cmnlib64.mbn' : 'cmnlib64bak',
   'cmnlib.mbn' : 'cmnlibbak',
   'hyp.mbn' : 'hypbak',
   'tz.mbn' : 'tzbak',
   'abl.elf' : 'ablbak',
   'keymaster.mbn' : 'keymasterbak',
   'xbl.elf' : 'xblbak',
   'rpm.mbn' : 'rpmbak',
   'NON-HLOS.bin' : 'modem',
   'static_nvbk.bin' : 'oem_stanvbk',
   'adspso.bin' : 'dsp',
   'BTFM.bin' : 'bluetooth',
   'logo.bin' : 'LOGO'
}

def FullOTA_InstallEnd(info):
  info.script.Print("Writing images...")
  for k, v in image_partitions.iteritems():
    try:
      img_file = info.input_zip.read("firmware/" + k)
      InstallImage(k, img_file, v, info)
    except KeyError:
      print "warning: no " + k + " image in input target_files; not flashing " + k

