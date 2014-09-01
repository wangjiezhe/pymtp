#!/usr/bin/env python3
#
# PyMTP Demo program
# (c) 2008 Nick Devito
# Released under the GPL-3
#

import sys
sys.path.insert(0, "../")  # so the examples work out of the box
import pymtp


def cdec(name):
    """Check if it's not None and decode"""
    return name is not None and name.decode() or None


def main():
    # Connect to MTP
    mtp = pymtp.MTP()
    mtp.connect()

    # Print out the device info
    print("Device Name\t\t: %s" % cdec(mtp.get_devicename()))
    print("Device Manufacturer\t: %s" % cdec(mtp.get_manufacturer()))
    print("Device Model Name\t: %s" % cdec(mtp.get_modelname()))
    print("Serial Number\t\t: %s" % cdec(mtp.get_serialnumber()))
    print("Battery Level\t\t: Max:%s/Cur:%s (%.2f%%)" % (mtp.get_batterylevel()[0], mtp.get_batterylevel()[1], ((float(mtp.get_batterylevel()[1])/float(mtp.get_batterylevel()[0]))*100)))
    print("Device Version\t\t: %s" % cdec(mtp.get_deviceversion()))
    print("Total Storage\t\t: %s bytes" % (mtp.get_totalspace()))
    print("Free Storage\t\t: %s bytes" % (mtp.get_freespace()))
    print("Used Storage\t\t: %s bytes (%.2f%%)" % (mtp.get_usedspace(),
                                                   mtp.get_usedspace_percent()))
    # Print out the folders
    print("Parent folders\t\t:")
    for folder in mtp.get_parent_folders():
        print("\t\t\t %s (id: %s)" % (cdec(folder.name), folder.folder_id))

    print("All folders\t\t:")
    folders = mtp.get_folder_list()
    for key in folders:
        folder = folders[key]
        print("\t\t\t %s (id: %s, parent: %s)" % (cdec(folder.name),
                                                  folder.folder_id,
                                                  folder.parent_id))

    # Print out the file and track listings
    print("File listing\t\t:")
    for devfile in mtp.get_filelisting():
        print("\t\t\t %s (id: %s / %s bytes)" % (cdec(devfile.filename),
                                                 devfile.item_id,
                                                 devfile.filesize))

    print("Track listing\t\t:")
    for track in mtp.get_tracklisting():
        print("\t\t\t%s - %s (%s / %s bytes)" % (cdec(track.artist),
                                                 cdec(track.title),
                                                 cdec(track.filename),
                                                 track.filesize))
    print("Playlist listing\t\t:")
    for playlist in mtp.get_playlists():
        print("\t\t\t%s (id: %s / %s tracks)" % (cdec(playlist.name),
                                                 playlist.playlist_id,
                                                 playlist.no_tracks))
        for track in playlist.tracks:
            try:
                info = mtp.get_track_metadata(track)
                print("\t\t\t\t%s - %s" % (cdec(info.artist),
                                           cdec(info.title)))
            except pymtp.ObjectNotFound:
                break

    # Disconnect from the device
    mtp.disconnect()


if __name__ == "__main__":
    main()
