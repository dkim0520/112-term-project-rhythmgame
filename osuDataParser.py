###Osu! file Data Parser###
###David Kim, davidk2###

#HitObject format: x, y, time, type, hitSound, extras (default is 0:0:0:0:)
#                                              sampleSet: additionSet:customIndex:sampleVolume:filename
#only need y, time, type, and end Y for sliders, 
#number of times going over slider can determine length of corresponding platform
import io
import os
import string
def getHitObject(osuFile):
    hitObjectsFound = False
    with io.open("Songs" + os.sep + osuFile, "r", encoding = "utf-8") as f:
        for line in f.readlines():
            if '[HitObjects]' in line:
                hitObjectsFound = True
            elif hitObjectsFound == True:
                with io.open("%s hitObjects" %(osuFile), "a", encoding = "utf-8") as g:
                    g.write(line)
    return ("%s hitObjects" %(osuFile))

def parseHitObjectData(hitFile):
    with io.open(hitFile, "r", encoding = "utf-8") as f:
        resultTuples = []
        for line in f.readlines():
            count = 0
            result = []
            for info in line.split(","):
                count += 1
                if count == 2:
                    result.append(int(info))
                elif count == 3:
                    result.append(int(info))
                elif count == 4:
                    result.append(int(info))
                elif count == 6:
                    result.append(info.strip())
            resultTuples.append(tuple(result))
            result = []
        return resultTuples