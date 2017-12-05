'''
ISTA 422 Final Project
Team Name: Monarch 2.0
Code Author: Phillip Johnson
Purpose of script:
	This Python script is used to clean and organize data from iNaturalist Gbif dump 
	and eButterfly Database dump and integrate it into a singular file in a format needed
	to run the R Species Distribution Model program. For additional information about specific 
	functionality of this code, please see additional comments included in the code below.
'''
#import csv utilizes the Python library that specializes in CSV manipulation and file writing.
import csv
'''
Global Variables:
	This predetermines items that will been to be reference throughout the different functions
	without having to explicitely return them from each function.
'''

year_keys=[]
month_list=['01','02','03','04','05','06','07','08','09','10','11','12','all']
data_dict={}


'''
Function get_iNat:
	This function opens and reads data from iNaturalist, in the form of the Gbif data dump. Once 
	open, it traverses the file, creating a dictionary association of each entry by scientificName,
	year, month, latitude, and longitude. While accomplishing this, it also does not transcribe
	any data that is not marked as 'Research Grade' or any data that is missing information in the areas
	needed. This function returns None, but rather fills the data_dict global variable.
'''
def get_iNat(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
			if row['scientificName'] not in data_keys and row['datasetName'] == 'iNaturalist research-grade observations':
				data_dict[row['scientificName']]= {}				
				'''
				organizing dictionary input into format {{year}, {month}, [lat, long]}
				'''
				if row['eventDate'][4]=='-':
					data_dict[row['scientificName']][row['eventDate'][0:4]]={}
					data_dict[row['scientificName']][row['eventDate'][0:4]]['01']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['02']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['03']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['04']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['05']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['06']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['07']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['08']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['09']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['10']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['11']=[]
					data_dict[row['scientificName']][row['eventDate'][0:4]]['12']=[]
					
					
					#format is Latitude, longitude
					data_dict[row['scientificName']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
					
					
			elif row['datasetName'] == 'iNaturalist research-grade observations':	
				'''
				This gets rid of all non research grade observations
				'''	
				if len(row['eventDate'])>0 and row['eventDate'][4]=='-':
					year_key = data_dict[row['scientificName']].keys()
					if row['eventDate'][0:4]not in year_key:
						year_keys.append([row['eventDate'][0:4]])
						data_dict[row['scientificName']][row['eventDate'][0:4]]={}
						data_dict[row['scientificName']][row['eventDate'][0:4]]['01']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['02']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['03']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['04']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['05']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['06']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['07']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['08']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['09']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['10']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['11']=[]
						data_dict[row['scientificName']][row['eventDate'][0:4]]['12']=[]
						'''
						Checking that entries have Lat/long coords, not transcribing entries if they do not.
						'''
						if len(row['decimalLatitude']) > 1 or len(row['decimalLongitude']) > 1:
							data_dict[row['scientificName']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])

					else:
						if len(row['decimalLatitude']) > 1 or len(row['decimalLongitude']) > 1:

							data_dict[row['scientificName']][row['eventDate'][0:4]][row['eventDate'][5:7]].append([row['decimalLatitude'],row['decimalLongitude']])
				

			
'''
Function get_eButterfly:
	This function opens and reads data from a csv file created from the eButterfly sql data dump 
	(this datadump is partially cleaned and extracted via a seperate script). Once open, it traverses 
	the file, creating a dictionary association of each entry by scientificName 
	(in this files case, it is labeled latin_name), year, month, latitude, and longitude. While 
	accomplishing this, it also does not transcribe any data that is missing information in the areas
	needed. This function returns None, but rather fills/augments the data_dict global variable.
'''
def get_eButterfly(filename):
	with open(filename,  encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		data_keys=data_dict.keys()
		for row in reader:
		#row['ColumnID'] = total_rows['ColumnID'].astype(str)
			if row['latin_name'] not in data_keys:
				data_dict[row['latin_name']]= {}				
				'''
				organizing dictionary input into format {{year}, {month}, [lat, long]}
				'''
				
				if len(row['year_created'])==4:
					data_dict[row['latin_name']][row['year_created']]={}
					data_dict[row['latin_name']][row['year_created']]['01']=[]
					data_dict[row['latin_name']][row['year_created']]['02']=[]
					data_dict[row['latin_name']][row['year_created']]['03']=[]
					data_dict[row['latin_name']][row['year_created']]['04']=[]
					data_dict[row['latin_name']][row['year_created']]['05']=[]
					data_dict[row['latin_name']][row['year_created']]['06']=[]
					data_dict[row['latin_name']][row['year_created']]['07']=[]
					data_dict[row['latin_name']][row['year_created']]['08']=[]
					data_dict[row['latin_name']][row['year_created']]['09']=[]
					data_dict[row['latin_name']][row['year_created']]['10']=[]
					data_dict[row['latin_name']][row['year_created']]['11']=[]
					data_dict[row['latin_name']][row['year_created']]['12']=[]
					#cleaning month formatting vvv
					if len(row['month_created']) == 1:
						row['month_created']='0' + row['month_created']
					#format is Latitude, longitude
					data_dict[row['latin_name']][row['year_created']][row['month_created']].append([row['latitude'],row['longitude']])
					
					
			else :	
				
				year_key = data_dict[row['latin_name']].keys()
				if row['year_created'] not in year_key:
					year_keys.append([row['year_created']])
					data_dict[row['latin_name']][row['year_created']]={}
					data_dict[row['latin_name']][row['year_created']]['01']=[]
					data_dict[row['latin_name']][row['year_created']]['02']=[]
					data_dict[row['latin_name']][row['year_created']]['03']=[]
					data_dict[row['latin_name']][row['year_created']]['04']=[]
					data_dict[row['latin_name']][row['year_created']]['05']=[]
					data_dict[row['latin_name']][row['year_created']]['06']=[]
					data_dict[row['latin_name']][row['year_created']]['07']=[]
					data_dict[row['latin_name']][row['year_created']]['08']=[]
					data_dict[row['latin_name']][row['year_created']]['09']=[]
					data_dict[row['latin_name']][row['year_created']]['10']=[]
					data_dict[row['latin_name']][row['year_created']]['11']=[]
					data_dict[row['latin_name']][row['year_created']]['12']=[]
					#cleaning month formatting vvv
					if len(row['month_created']) == 1:
						row['month_created']='0' + row['month_created']
					'''
					Checking that entries have Lat/long coords, not transcribing entries if they do not.
					'''
						
					if len(row['latitude']) > 1 or len(row['longitude']) > 1:
						data_dict[row['latin_name']][row['year_created']][row['month_created']].append([row['latitude'],row['longitude']])

				else:
					if len(row['month_created']) == 1:
						row['month_created']='0' + row['month_created']
					if len(row['latitude']) > 1 or len(row['longitude']) > 1:

						data_dict[row['latin_name']][row['year_created']][row['month_created']].append([row['latitude'],row['longitude']])
			


#Runs get_iNat function and organizes/cleans observations.csv file from the Gbif Datadump (iNaturalist)
print('Beginning cleaning of iNaturalist Data')
get_iNat('observations.csv')
print('Cleaning of iNaturalist Data Complete')
print('Beginning cleaning of eButterfly Data')
#Runs get_eButterfly function and organizes/cleans eb_butterflies_new.csv file from the eButterfly Datadump.
get_eButterfly('eb_butterflies_new.csv')
print('Processing Complete, beginning file creation and integration of data sources')

''' Writing data in format needed to new TXT file for SDM format

***************************************************************************************************
	If preferred format is TXT and not CSV please uncomment out this function. 
		To do this, please move contents from below "print('data_for_sdm.txt created successfully')" 
		to directly under the astrics line below.
***************************************************************************************************

with open('data_for_sdm.txt','w', encoding='utf-8') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',')

	csvwriter.writerow(['scientificName','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

					
print('data_for_sdm.txt created successfully')
'''


'''					
This portion of code takes the filled global variable data_dict and creates a
	csv file which will be used by the Species Distribution Model (SDM) as well
	as allowing easier user viewing if further or seperate analysis is needed on 
	the combined, cleaned datasets.
'''
#Format of CSV is scientificName, year, month, latitude, longitude
with open('data_for_sdm.csv','w', encoding='utf-8') as csv_file:
	csvwriter = csv.writer(csv_file, delimiter=',' )

	csvwriter.writerow(['scientificName','year','month','latitude','longitude'])

	for id in data_dict:
		for year in data_dict[id]:
			for month in data_dict[id][year]:
				for coords in data_dict[id][year][month]:
					csvwriter.writerow([id,year, month,coords[0], coords[-1]])

	
print('data_for_sdm.csv created successfully. This is useful for visualizing the data in a clean excel form')


#In Progress
'''
This portion of code seperates each Species into their own files, containing all
of the data for that species in the format scientificName, year, month, latitude, 
longitude. When this code finishes running there will be a singular csv for each 
and every species.
'''

print('Beginning species specific csv file creation.')
species=list(data_dict.keys())
for i in range(len(species)):
	nameset=species[i]
	naming=nameset.split()
	for j in range(len(naming)):
		naming[j]=naming[j].strip('"')
		for char in naming[j]:
			if char in " ?.!/;:":
				naming[j] = naming[j].replace(char,'')
	join_name='_'.join(naming)
	filename = str(join_name + '.csv')
	with open(filename,'w') as csv_file:
		csvwriter = csv.writer(csv_file, delimiter=',' )
		csvwriter.writerow(['year','month','latitude','longitude'])
		for year in data_dict[nameset]:
			for month in data_dict[nameset][year]:
				for lat in data_dict[nameset][year][month]:
					csvwriter.writerow([year, month,coords[0], coords[-1]])


print('Individual species csv file creation complete.')