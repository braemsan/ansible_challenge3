import pandas

# UNI DATA

#read csv that is FROM the unzipping in step 3
df = pandas.read_csv('./universities-intake-enrolment-and-graduates-by-course.csv')

print(df)
#remove comma from numbers in graduates column
df['graduates'] = df['graduates'].str.replace(',', '')
print(df['graduates'])

#filter out IT course and MF sex
filtered = df[(df.course=="Information Technology") & (df.sex=="MF")]
print(filtered)

#save to csv without the first column index
filtered.to_csv('./6.filtered_data_from_university_with_all_the_numbers_i_want.csv', index=False)

unidf = pandas.read_csv('./6.filtered_data_from_university_with_all_the_numbers_i_want.csv')
print(unidf)

#sum total of uni IT graduates and it's grabbing from `unidf`, variable NOT the CSV FILE
TotalUni = unidf['graduates'].sum()
print (f"Total Uni graduates: {TotalUni}")

#write total to unidf and produce a CSV file 
unidf.loc['TotalUni'] = pandas.Series(unidf['graduates'].sum(), index = ['graduates'])
unidf.to_csv('./7.sum_of_graduate_from_university_enrollment_only.csv', index=False)


# DO THE SAME FOR POLY DATA HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#reading of csv that is FROM the unzipping in step 4
df2 = pandas.read_csv('./polytechnics-intake-enrolment-and-graduates-by-course.csv')
df2['graduates'] = df['graduates'].str.replace(',', '')

#filter out IT course and MF sex
filtered2 = df[(df.course=="Information Technology") & (df.sex=="MF")]

#save to csv
filtered2.to_csv('./8.filtered_data_from_poly_with_all_the_numbers_i_want.csv', index=False)

polydf = pandas.read_csv('./8.filtered_data_from_poly_with_all_the_numbers_i_want.csv')
print(polydf)
TotalPoly = polydf['graduates'].sum()
print (f"Total Poly graduates: {TotalPoly}")

polydf.loc['TotalPoly'] = pandas.Series(polydf['graduates'].sum(), index = ['graduates'])
polydf.to_csv('./9.sum_of_graduate_from_university_and_poly_enrollment_together.csv', index=False)



# FINAL STEP TO ADD UP BOTH NUMBER
GrandTotal = TotalPoly + TotalUni
print(f"Total IT graduates in Uni and Poly: {GrandTotal}")