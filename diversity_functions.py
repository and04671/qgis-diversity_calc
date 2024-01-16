
import math


def dc_summarizePoly(poly, lyrPoint, fldSpecies):
	dctPoly = {}
	for obs in lyrPoint.getFeatures(poly.geometry().boundingBox()):
		if poly.geometry().contains(obs.geometry()):
			sSpecies = obs.attribute(fldSpecies)
			if sSpecies in dctPoly.keys():
				dctPoly[sSpecies] += 1
			else:
				dctPoly[sSpecies] = 1

	return dctPoly

def dc_mergeDictionaries(dMain, cat, dPoly):
	if cat in dMain.keys():
		for species, obs in dPoly.items():
			if species in dMain[cat].keys():
				dMain[cat][species] += obs
			else:
				dMain[cat][species] += obs
	else:
		dMain[cat] = dPoly

	return dMain

def dc_richness(dict):
	return len(dict)

def dc_shannons(dict):
	total = sum(dict.values())
	shannons = 0;
	for count in dict.values():
		prop = count/total
		shannons += prop*math.log(prop)
	return abs(shannons);

def dc_simpsons(dict):
	total = sum(dict.values())
	simpsons = 0;
	for count in dict.values():
		prop = count/total
		simpsons += prop*prop
	return simpsons;

def dc_evenness(dict):
	max = math.log(dc_richness(dict))
	return dc_shannons(dict)/max

def dc_resultString(dict):
	result = ""
	for category, summary in dict.items():
		result += "{}: {} {:2.3f} {:2.3f} {:2.3f}\n".format(category, dc_richness(summary), dc_shannons(summary), dc_simpsons(summary), dc_evenness(summary))
	return result
