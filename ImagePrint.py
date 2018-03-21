# ImagePrint.py
# Copyright (c) 2008-2017 Chris Gonnerman
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions
# are met:
# 
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer. 
# 
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution. 
# 
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
ImagePrint.py defines a class for generating images, using the same "printing"
interface as MSWinPrint.py.  Combined with MetaPrint.py, it can be used to
create print previews.

document is a class for creating and running print jobs.  Presently, the 
source is the only documentation for this class.
"""

import Image, ImageDraw, ImageFont

# assuming 72 dpi, so as to match the font scaling

papersizes = {
    # width, height
    "letter":       (612, 792),
    "legal":        (612, 1008),
    "fanfold":      (1071, 792),
}

orientations = {
    "portrait":     1,
    "landscape":    2,
}

duplexes = {
    "normal":       1,
    "long":         2,
    "short":        3,
}

fontpath = "c:/windows/fonts/%s.ttf"

# normal, italic, bold, bold italic

fontmap = {
    "Times New Roman": 
        ("times", "timesi", "timesbd", "timesbi"),
    "Arial": 
        ("arial", "ariali", "arialbd", "arialbi"),
    "Arial Narrow": 
        ("arialn", "arialni", "arialnb", "arialnbi"),
    "Lucida Console":
        ("lucon", "lucon", "lucon", "lucon"),
    "Free 3 of 9 Extended Regular":
        ("fre3of9x", "fre3of9x", "fre3of9x", "fre3of9x"),
}

# unlike other printing modules, this module retains just one
# page image... the last one printed.

class document:

    def __init__(self, papersize = "letter", 
            orientation = "portrait", duplex = "normal"):
        self.font = None
        self.papersize = papersize
        self.orientation = orientations[orientation]
        self.imagesize = papersizes[papersize]
        self.duplex = duplex # ignored here anyway
        if self.orientation == 2:
            self.imagesize = (self.imagesize[1], self.imagesize[0])
        self.newimage()

    def newimage(self):
        self.Image = Image.new("RGB", self.imagesize, (255, 255, 255))
        self.draw = ImageDraw.Draw(self.Image)
        self.reset = 0

    def begin_document(self, desc = "ImagePrint.py print job"):
        pass

    def end_document(self):
        pass

    def end_page(self):
        self.reset = 1

    def line(self, from_, to):
        if self.reset:
            self.newimage()
        self.draw.line(( from_, to ), fill = self.ink)

    def rectangle(self, box):
        if self.reset:
            self.newimage()
        self.draw.line(((box[0], box[1]), (box[2], box[1])), fill = self.ink)
        self.draw.line(((box[2], box[1]), (box[2], box[3])), fill = self.ink)
        self.draw.line(((box[2], box[3]), (box[0], box[3])), fill = self.ink)
        self.draw.line(((box[0], box[3]), (box[0], box[1])), fill = self.ink)

    def text(self, position, text):
        if self.reset:
            self.newimage()
        self.draw.text(position, text, font = self.font, fill = self.ink)

    def setfont(self, name, size, bold = None, italic = None):
        if self.reset:
            self.newimage()
        try:
            fontset = fontmap[name]
        except:
            print "Unknown Font:", name
            raise
        fontid = 0
        if bold:
            fontid += 2
        if italic:
            fontid += 1
        fontfile = fontpath % fontset[fontid]
        self.font = ImageFont.truetype(fontfile, size)

    def image(self, position, image, size):
        if self.reset:
            self.newimage()
        self.Image.paste(image.resize(size, Image.ANTIALIAS), position)

    def setink(self, ink):
        if self.reset:
            self.newimage()
        self.ink = ink

    def setfill(self, onoff):
        if self.reset:
            self.newimage()


# end of file.
