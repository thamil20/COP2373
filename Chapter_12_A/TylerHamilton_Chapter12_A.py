import numpy as np


def import_data(file):
    # Import the .csv file into a numpy array
    return np.genfromtxt(file, delimiter=',', dtype=None, encoding=None)


def per_exam_calculations(exam_data):
    # calculate mean, median, standard deviation, minimum, maximum for all exams.
    exam_data = exam_data.T
    # Mean
    means = np.mean(exam_data, axis=1)
    # Median
    medians = np.median(exam_data, axis=1)
    # Standard Deviation
    stddevs = np.std(exam_data, axis=1)
    # Minimum
    minimums = np.min(exam_data, axis=1)
    # Maximum
    maximums = np.max(exam_data, axis=1)
    return [means, medians, stddevs, minimums, maximums]


def all_exam_calculations(exam_data):
    # calculate mean, median, standard deviation, minimum, maximum for all exams.
    exam_data = exam_data.T
    # Mean
    all_mean = np.mean(exam_data)
    # Median
    all_median = np.median(exam_data)
    # Standard Deviation
    all_stddev = np.std(exam_data)
    # Minimum
    all_mini = np.min(exam_data)
    # Maximum
    all_maxi = np.max(exam_data)
    return [all_mean, all_median, all_stddev, all_mini, all_maxi]


def pass_or_fail(exam_data, exam_num):
    # Determine and print the number of students who scored >60% on each exam.
    
    # A counter variable to count the amount of passing grades.
    count = 0
    # Iterate over an exam's scores and count how many students passed.
    for score in exam_data.T[exam_num-1]:
        # Determine if a grade is less than 60, if so, continue.
        if score < 60:
            continue
        # Determine if a grade is greater than or equal to 60, 
        # if so, count that as a passing grade.
        elif score >= 60:
            count += 1
    # Calculate the percentage of passing grades.
    pass_percent = count/len(exam_data.T[exam_num-1])*100
    return pass_percent


def overall_pass_percentage(exam_data):
    # Calculate and print the overall pass percentage across all exams.
    # Save the previously calculated pass_percents in variables
    exam_1 = pass_or_fail(exam_data,1)
    exam_2 = pass_or_fail(exam_data,2)
    exam_3 = pass_or_fail(exam_data,3)
    # Divide the sum of the exam pass percentages by the number of rows.
    overall = (exam_1+exam_2+exam_3)/exam_data.T.shape[0]
    return overall
    


def main():
    file = str(input("Please enter the name and " 
                     "extension of the file you wish to use "
                     "(grades.csv): "))
    # Save the numpy array to a variable
    exam_data = import_data(file)
    # Save the header in a variable
    header = exam_data[0]
    # Print the header
    print("\n---- Example Data ----\n")
    print(', '.join(header))
    # Print the first 3 rows of data
    for i in range(1,4):
        print(', '.join(exam_data[i]))
    
    # Format the data to be all integers.
    exam_data = np.delete(exam_data, [0,1], 1)
    exam_data = np.delete(exam_data, 0, 0)
    exam_data = np.ndarray.astype(exam_data, int)
    
    # Save means, medians, standard deviations, minimums, and maximums in variables.
    means = per_exam_calculations(exam_data)[0]
    medians  = per_exam_calculations(exam_data)[1]
    stddevs  = per_exam_calculations(exam_data)[2]
    mins  = per_exam_calculations(exam_data)[3]
    maxs  = per_exam_calculations(exam_data)[4]
    all_exams = all_exam_calculations(exam_data)
    
    print("\n---- Data Analysis ----")
    
    # Display each exam's means, medians, standard deviations, minimums, and maximums.
    print(f'\nMean of exam 1: {means[0]:.2f},' 
          f'\nMedian of exam 1: {medians[0]:.2f},' 
          f'\nStandarad Deviation of exam 1: {stddevs[0]:.2f},' 
          f'\nMinimum of exam 1: {mins[0]:.2f},'
          f'\nMaximum of exam 1: {maxs[0]:.2f}')
    
    print(f'\nMean of exam 2: {means[1]:.2f},' 
          f'\nMedian of exam 2: {medians[1]:.2f},' 
          f'\nStandarad Deviation of exam 2: {stddevs[1]:.2f},' 
          f'\nMinimum of exam 2: {mins[1]:.2f},'
          f'\nMaximum of exam 2: {maxs[1]:.2f}')

    print(f'\nMean of exam 3: {means[2]:.2f},' 
          f'\nMedian of exam 3: {medians[2]:.2f},' 
          f'\nStandarad Deviation of exam 3: {stddevs[2]:.2f},' 
          f'\nMinimum of exam 3: {mins[2]:.2f},'
          f'\nMaximum of exam 3: {maxs[2]:.2f}')
    
    # Display the mean, median, standard deviation, minumum and maximum of all exams.
    print(f'\nMean of all exams: {all_exams[0]:.2f},' 
          f'\nMedian of all exams: {all_exams[1]:.2f},' 
          f'\nStandarad Deviation of all exams: {all_exams[2]:.2f},' 
          f'\nMinimum of all exams: {all_exams[3]:.2f},'
          f'\nMaximum of all exams: {all_exams[4]:.2f}')
    
    # Save each exam's pass_percent in variables.
    exam_1_pass_percent = pass_or_fail(exam_data,1)
    exam_2_pass_percent = pass_or_fail(exam_data,2)
    exam_3_pass_percent = pass_or_fail(exam_data,3)
    all_pass_percentage = overall_pass_percentage(exam_data)
    
    # Display each exam's passing percentage to the user.
    print(f'\n{exam_1_pass_percent}% of students passed exam 1.'
          f'\n{exam_2_pass_percent}% of students passed exam 2.'
          f'\n{exam_3_pass_percent}% of students passed exam 3.'
    )

    # Display the overall
    print(f'\n{all_pass_percentage:.2f}% of students passed across all exams.')
    
# Run the main function
if __name__ == '__main__':
    main()
    
    # Edit - Changed np.astype() to np.ndarray.astype() in an attempt to allow my instructor to run the code
    #        without receiving an error stating np.astype() does not exist.
    
    # Output did not change after the edit:
    
    # Please enter the name and extension of the file you wish to use (grades.csv): Chapter_12_A/grades.csv

    # ---- Example Data ----

    # First Name, Last Name, Exam 1, Exam 2, Exam 3
    # Tyler, Hamilton, 15, 25, 90
    # Danny, Phantom, 25, 16, 14
    # Jimmy, Neutron, 90, 99, 100

    # ---- Data Analysis ----

    # Mean of exam 1: 68.60,
    # Median of exam 1: 78.50,
    # Standarad Deviation of exam 1: 28.65,
    # Minimum of exam 1: 15.00,
    # Maximum of exam 1: 100.00

    # Mean of exam 2: 54.10,
    # Median of exam 2: 56.00,
    # Standarad Deviation of exam 2: 34.94,
    # Minimum of exam 2: 1.00,
    # Maximum of exam 2: 99.00

    # Mean of exam 3: 82.20,
    # Median of exam 3: 89.50,
    # Standarad Deviation of exam 3: 24.08,
    # Minimum of exam 3: 14.00,
    # Maximum of exam 3: 100.00

    # Mean of all exams: 68.30,
    # Median of all exams: 82.50,
    # Standarad Deviation of all exams: 31.71,
    # Minimum of all exams: 1.00,
    # Maximum of all exams: 100.00

    # 70.0% of students passed exam 1.
    # 50.0% of students passed exam 2.
    # 90.0% of students passed exam 3.

    # 70.00% of students passed across all exams.
    
    # End of Output