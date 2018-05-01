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
    with io.open(osuFile, "r", encoding = "utf-8") as f:
        for line in f.readlines():
            if "AudioFilename" in line:
                with io.open("%s hitObjects" %(osuFile), "a", encoding = "utf-8") as g:
                    g.write(line)
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
                if info[:15] == "AudioFilename: ":
                    resultTuples.append((info.strip()))
                count += 1
                if count == 2:
                    result.append(int(info))
                elif count == 3:
                    result.append(int(info))
                elif count == 4:
                    result.append(int(info))
            resultTuples.append(result)
        resultTuples.pop(1)
        musicName = ""
        for hits in range(len(resultTuples)):
            if "AudioFilename: " in resultTuples[hits]:
                musicName = resultTuples[hits]
            elif isinstance(resultTuples[hits-1][0], int) and abs(resultTuples[hits][0] - resultTuples[hits - 1][0]) > 50:
                resultTuples[hits][0] = resultTuples[hits-1][0] + (resultTuples[hits][0] - resultTuples[hits - 1][0])
            resultTuples[hits] = tuple(resultTuples[hits])
        return (resultTuples[1:],musicName[15:])

#print(parseHitObjectData(getHitObject("Songs\Kero Kero Bonito - Flamingo (staszek00700) [Insane].osu")))
#print(len(parseHitObjectData(getHitObject("Songs\Bowling For Soup - 1985 (Voli) ['85].osu"))))