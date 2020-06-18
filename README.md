# Video_analytics
1. Following dependencies are required to proceed with the code
	a. Python 3.6 or recent.
	b. Pandas
	c. Numpy
  	d. xlrd
	e. Keras
	f. Tensorflow
	g. OpenCV
	h. MoviePy
	i. Matplotlib 

2. ‘VA_Baby_details_data.xlsx’ contains UHID, birthweight, gestational age and gender of each   patient.

3. ‘video_tags (13).xlsx’ contains the UHIDs, name of the videos along with manipulation found in  each of them.  

3. Use ‘count_total_frames.ipynb’ to count total number of frames recorded, total duration of video data recorded, number of frames of diaper change, feeding and patting and mean duration of diaper change, feeding and patting.

4. Use ‘HistogramStacked.ipynb’ to divide the duration of procedures in different buckets for histogram analysis.

5. ‘27april_full.xlsx’ has the histogram prepared in ‘Sheet2’ according to the buckets generated in above step.

6. Use ‘new_fps15set.ipynb’ to set the frame rate of videos containing considered manipulations to 15 fps.

7. Use ‘frameExtraction.py’ to extract the frames of labelled manipulations (diaper change, feeding, patting).

8. 'kalawati_tags.ipynb' & 'apollo_tags.ipynb' is used to calulate mean and STV for HR and SpO2, for pre, post and during procedure

9. 'Kalawati_new.ipynb' & 'Apollo_new.ipynb' is used to convert the time-zones and extract meta-data from the file names.

10. 'Hypothesis testing.ipybb' this notebook is used to calculate p values between pre, post and during procedure

11. 'Plotting_procedure.ipynb' this notebook is used to plot the procedures

12. 'kalawati_data_prep.ipynb' & 'apollo_data_prep.ipynb' is used to extract data from the database and map it to the procedure time.

13. 'CNN.ipynb' this notebook is used for Transfer learning

14. 'LSTM_with_zero_padding_2.ipynb' LSTM model for ptrediction

15. 'Leave_one_out.ipynb' this notebook implements Leave one out CV, uhid wise








  
