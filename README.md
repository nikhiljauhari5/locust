

# To run the locust files 

locust -f filename.py


# To run correlation file

locust -f correlation.py -u 1 -r 1 -t 20s --headless --only-summary 
