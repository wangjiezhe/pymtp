#!/usr/bin/env python3
#
# PyMTP demo scripts
# (c) 2008 Nick Devito
# Released under the GPL v3 or later.
#

import sys
sys.path.insert(0, "../")

import pymtp
import stagger


def usage():
    print("Usage: %s <source> <target> <parent>\n\
(The parent id can be 0 for the root directory)" % (sys.argv[0]))


def cenc(name):
    """Check if it's not None and encode"""
    return name is not None and name.encode() or None


def main():
    if len(sys.argv) <= 3:
        usage()
        sys.exit(2)

    mtp = pymtp.MTP()
    mtp.connect()

    source = sys.argv[1]
    target = sys.argv[2]
    parent = int(sys.argv[3])

    tag = stagger.read_tag(source)

    metadata = pymtp.LIBMTP_Track()

    if hasattr(tag, 'artist'):
        metadata.artist = cenc(tag.artist)
    if hasattr(tag, 'title'):
        metadata.title = cenc(tag.title)
    if hasattr(tag, 'album'):
        metadata.album = cenc(tag.album)
    if hasattr(tag, 'track'):
        metadata.tracknumber = tag.track

    track_id = mtp.send_track_from_file(source, target,
                                        metadata, parent=parent)
    print("Created new track with ID: %s" % (track_id))
    mtp.disconnect()

if __name__ == "__main__":
    main()
