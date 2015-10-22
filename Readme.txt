##
#Description	Spin up Amazon ES2 instances using Python SDK
#Author:	Saahil Pingle
## 

How to launch the program?
python launcher.py no_of_instances instance_region activity

The program accepts 3 command line arguments
1. no of instances
2. instance region
3. activity to be performed (start or stop)

If activity is start, then the said number of EC2 instances will be spinned up in the said region.
Once the instances are started, the user is provided with a choice of 3 things:
1. to terminate all instances spinned in the current session
2. to terminate only a give instacnce by providing the instance ID
3. to exit the system, and keep the state of the instances as it is.

If the user selects option (1), all the instances will be terminated.
If the user selects option (2), only the instance with the provided instance ID will be terminated
If the user selects option (3), the program will be terminated

If the activity is stop:
1. the instance region is just used to ensure connection to AWS.
2. no of instances cmd line argument == no of actually running instances in AWS => instance is terminated.
3. no of instances cmd line argument > no of actually running instances in AWS (>1) => all running instances will be terminated
4. no of instances cmd line argument > no of actually running instances in AWS (0) => Warning will be displayed

The program consists for 3 major functions
1. getConnectionInstance()
takes in the region as input argument and initiates a connection with Amazon AWS.
on line 7 provide the required access key and secret key.

2. startInstance()
takes in the number of isntances and the instance region as input arguments and spins up ES2 instances in the said region.

3. stopInstance()
takes in the number of instances and the instance region and an optional argument 'instance ID' and then terminates the said instance(s).

Limitations:
1. Hadling of 0 no of instances is not specifically taken into consideration
2. While terminating using instance ID, only a single instance ID is accepted to ensure the terminate() function is called properly => not included accepting multiple instance IDs from user.
3. Assumed that the user provides well formated values for 'no of instances', 'instance region' and 'activity' cmd line arguments i.e. no negative values, instance region is as required by AWS API, all lowercase respectively.
4. All test cases are not covered.
eg. if terminating using instance ID, if the entered instance ID is already terminated, no warning/error is provided, instead the terminate() function is called on again.
5. Case of blank Access Key and Secret key is not specifically handled.