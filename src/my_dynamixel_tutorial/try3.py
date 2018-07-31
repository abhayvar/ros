#!/usr/bin/env python
import roslib
roslib.load_manifest('my_dynamixel_tutorial')
import time
import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg 
import control_msgs.msg  
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal



class Joint:
        def __init__(self, motor_name):
            #arm_name should be b_arm or f_arm
            	self.name = motor_name   
		print(motor_name)        
		self.jta = actionlib.SimpleActionClient('/'+self.name+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
		rospy.loginfo('Waiting for joint trajectory action')
		self.jta.wait_for_server()
		rospy.loginfo('Found joint trajectory action!')

            
        def move_joint(self, angles):
            goal = FollowJointTrajectoryGoal()                  
            char = self.name[0] #either 'f' or 'b'
            goal.trajectory.joint_names = ['motor6','motor3','motor2','motor4','motor7','motor1','motor5','motor8','motor9','motor10','motor11','motor12','motor13','motor14','motor15','motor16','motor17','motor19']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(1)              
            goal.trajectory.points.append(point)
            self.jta.send_goal_and_wait(goal)
              
                       #     6         3        2         4         7       1        5         8          9        10      11         12      13      14        15       16      17       19
def main():
	arm = Joint('f_arm')
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.149419,-0.008988,-0.370623,-0.008988,0.168469,0.530676,0.520042,-0.008988,-0.008988,0.362208,0.000000])
	time.sleep(5)
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.140025,-0.017974,-0.374960,-0.017974,0.178123,0.536245,0.514985,-0.017974,-0.017974,0.358122,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.130721,-0.026957,-0.379385,-0.026957,0.187861,0.541973,0.510106,-0.026957,-0.026957,0.354112,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.121507,-0.035936,-0.383902,-0.035936,0.197681,0.547857,0.505410,-0.035936,-0.035936,0.350176,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.112383,-0.044909,-0.388514,-0.044909,0.207581,0.553889,0.500897,-0.044909,-0.044909,0.346308,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.103349,-0.053875,-0.393221,-0.053875,0.217559,0.560063,0.496570,-0.053875,-0.053875,0.342504,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.094406,-0.062832,-0.398025,-0.062832,0.227612,0.566373,0.492431,-0.062832,-0.062832,0.338761,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.085552,-0.071779,-0.402928,-0.071779,0.237738,0.572811,0.488480,-0.071779,-0.071779,0.335073,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.076786,-0.080714,-0.407930,-0.080714,0.247934,0.579371,0.484716,-0.080714,-0.080714,0.331437,0.000000])
	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.068107,-0.089637,-0.413032,-0.089637,0.258198,0.586045,0.481139,-0.089637,-0.089637,0.327847,0.000000])
	#arm.move_joint([0.000000,-0.193732,0.089012,-0.000000,-0.247837,-0.000000,0.310669,-0.161337,-0.089637,-0.478714,-0.089637,0.260102,0.582855,0.640050,-0.089637,-0.089637,0.322753,0.000000])
	#arm.move_joint([0.000000,-0.178024,0.073304,-0.000000,-0.251327,-0.000000,0.307178,-0.236831,-0.089637,-0.525089,-0.089637,0.261744,0.579146,0.761920,-0.089637,-0.089637,0.317402,0.000000])
	#arm.move_joint([0.000000,-0.162316,0.057596,-0.000000,-0.254818,-0.000000,0.303687,-0.301989,-0.089637,-0.559488,-0.089637,0.263190,0.575050,0.861477,-0.089637,-0.089637,0.311859,0.000000])
	#arm.move_joint([0.000000,-0.146608,0.041888,-0.000000,-0.258309,-0.000000,0.300197,-0.359837,-0.089637,-0.584907,-0.089637,0.264505,0.570699,0.944744,-0.089637,-0.089637,0.306194,0.000000])
	#arm.move_joint([0.000000,-0.130900,0.026180,-0.000000,-0.261799,-0.000000,0.296706,-0.411878,-0.089637,-0.602857,-0.089637,0.265758,0.566233,1.014735,-0.089637,-0.089637,0.300475,0.000000])
	#arm.move_joint([0.000000,-0.115192,0.010472,-0.000000,-0.265290,-0.000000,0.293215,-0.458900,-0.089637,-0.614189,-0.089637,0.267019,0.561793,1.073089,-0.089637,-0.089637,0.294774,0.000000])
	#arm.move_joint([0.000000,-0.099484,-0.005236,-0.000000,-0.268781,-0.000000,0.289725,-0.501287,-0.089637,-0.619410,-0.089637,0.268360,0.557524,1.120698,-0.089637,-0.089637,0.289164,0.000000])
	#arm.move_joint([0.000000,-0.083776,-0.020944,-0.000000,-0.272271,-0.000000,0.286234,-0.539164,-0.089637,-0.618834,-0.089637,0.269858,0.553578,1.157998,-0.089637,-0.089637,0.283719,0.000000])
	#arm.move_joint([0.000000,-0.068068,-0.036652,-0.000000,-0.275762,-0.000000,0.282743,-0.572462,-0.089637,-0.612649,-0.089637,0.271590,0.550108,1.185111,-0.089637,-0.089637,0.278517,0.000000])
	#arm.move_joint([0.000000,-0.052360,-0.052360,-0.000000,-0.279253,-0.000000,0.279253,-0.600957,-0.089637,-0.600957,-0.089637,0.273636,0.547271,1.201914,-0.089637,-0.089637,0.273636,0.000000])
	#arm.move_joint([0.000000,-0.036652,-0.068068,-0.000000,-0.282743,-0.000000,0.275762,-0.624288,-0.089637,-0.583785,-0.089637,0.276074,0.545226,1.208073,-0.089637,-0.089637,0.269152,0.000000])
	#arm.move_joint([0.000000,-0.020944,-0.083776,-0.000000,-0.286234,-0.000000,0.272271,-0.641960,-0.089637,-0.561078,-0.089637,0.278987,0.544131,1.203038,-0.089637,-0.089637,0.265144,0.000000])
	#arm.move_joint([0.000000,-0.005236,-0.099484,-0.000000,-0.289725,-0.000000,0.268781,-0.653335,-0.089637,-0.532673,-0.089637,0.282452,0.544140,1.186008,-0.089637,-0.089637,0.261688,0.000000])
	#arm.move_joint([0.000000,0.010472,-0.115192,-0.000000,-0.293215,-0.000000,0.265290,-0.657606,-0.089637,-0.498251,-0.089637,0.286546,0.545401,1.155857,-0.089637,-0.089637,0.258855,0.000000])
	#arm.move_joint([0.000000,0.026180,-0.130900,-0.000000,-0.296706,-0.000000,0.261799,-0.653730,-0.089637,-0.457253,-0.089637,0.291340,0.548053,1.110983,-0.089637,-0.089637,0.256713,0.000000])
	#arm.move_joint([0.000000,0.041888,-0.146608,-0.000000,-0.300197,-0.000000,0.258309,-0.640305,-0.089637,-0.408725,-0.089637,0.296901,0.552224,1.049031,-0.089637,-0.089637,0.255323,0.000000])
	#arm.move_joint([0.000000,0.057596,-0.162316,-0.000000,-0.303687,-0.000000,0.254818,-0.615291,-0.089637,-0.351027,-0.089637,0.303286,0.558024,0.966318,-0.089637,-0.089637,0.254738,0.000000])
	#arm.move_joint([0.000000,0.073304,-0.178024,-0.000000,-0.307178,-0.000000,0.251327,-0.575356,-0.089637,-0.281157,-0.089637,0.310547,0.565548,0.856513,-0.089637,-0.089637,0.255001,0.000000])
	#arm.move_joint([0.000000,0.089012,-0.193732,-0.000000,-0.310669,-0.000000,0.247837,-0.513981,-0.089637,-0.192841,-0.089637,0.318724,0.574870,0.706823,-0.089637,-0.089637,0.256147,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.413032,-0.089637,-0.068107,-0.089637,0.327847,0.586045,0.481139,-0.089637,-0.089637,0.258198,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.407930,-0.080714,-0.076786,-0.080714,0.331437,0.579371,0.484716,-0.080714,-0.080714,0.247934,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.402928,-0.071779,-0.085552,-0.071779,0.335073,0.572811,0.488480,-0.071779,-0.071779,0.237738,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.398025,-0.062832,-0.094406,-0.062832,0.338761,0.566373,0.492431,-0.062832,-0.062832,0.227612,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.393221,-0.053875,-0.103349,-0.053875,0.342504,0.560063,0.496570,-0.053875,-0.053875,0.217559,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.388514,-0.044909,-0.112383,-0.044909,0.346308,0.553889,0.500897,-0.044909,-0.044909,0.207581,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.383902,-0.035936,-0.121507,-0.035936,0.350176,0.547857,0.505410,-0.035936,-0.035936,0.197681,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.379385,-0.026957,-0.130721,-0.026957,0.354112,0.541973,0.510106,-0.026957,-0.026957,0.187861,0.000000])
	#arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.374960,-0.017974,-0.140025,-0.017974,0.358122,0.536245,0.514985,-0.017974,-0.017974,0.178123,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.370623,-0.008988,-0.149419,-0.008988,0.362208,0.530676,0.520042,-0.008988,-0.008988,0.168469,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.366374,-0.000000,-0.158900,-0.000000,0.366374,0.525274,0.525274,-0.000000,-0.000000,0.158900,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.362208,0.008988,-0.168469,0.008988,0.370623,0.520042,0.530676,0.008988,0.008988,0.149419,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.358122,0.017974,-0.178123,0.017974,0.374960,0.514985,0.536245,0.017974,0.017974,0.140025,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.354112,0.026957,-0.187861,0.026957,0.379385,0.510106,0.541973,0.026957,0.026957,0.130721,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.350176,0.035936,-0.197681,0.035936,0.383902,0.505410,0.547857,0.035936,0.035936,0.121507,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.346308,0.044909,-0.207581,0.044909,0.388514,0.500897,0.553889,0.044909,0.044909,0.112383,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.342504,0.053875,-0.217559,0.053875,0.393221,0.496570,0.560063,0.053875,0.053875,0.103349,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.338761,0.062832,-0.227612,0.062832,0.398025,0.492431,0.566373,0.062832,0.062832,0.094406,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.335073,0.071779,-0.237738,0.071779,0.402928,0.488480,0.572811,0.071779,0.071779,0.085552,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.331437,0.080714,-0.247934,0.080714,0.407930,0.484716,0.579371,0.080714,0.080714,0.076786,0.000000])
#	arm.move_joint([0.000000,0.104720,-0.209440,-0.000000,-0.314159,-0.000000,0.244346,-0.327847,0.089637,-0.258198,0.089637,0.413032,0.481139,0.586045,0.089637,0.089637,0.068107,0.000000])
#	arm.move_joint([0.000000,0.089012,-0.193732,-0.000000,-0.310669,-0.000000,0.247837,-0.322753,0.089637,-0.260102,0.089637,0.478714,0.640050,0.582855,0.089637,0.089637,0.161337,0.000000])
#	arm.move_joint([0.000000,0.073304,-0.178024,-0.000000,-0.307178,-0.000000,0.251327,-0.317402,0.089637,-0.261744,0.089637,0.525089,0.761920,0.579146,0.089637,0.089637,0.236831,0.000000])
#	arm.move_joint([0.000000,0.057596,-0.162316,-0.000000,-0.303687,-0.000000,0.254818,-0.311859,0.089637,-0.263190,0.089637,0.559488,0.861477,0.575050,0.089637,0.089637,0.301989,0.000000])
#	arm.move_joint([0.000000,0.041888,-0.146608,-0.000000,-0.300197,-0.000000,0.258309,-0.306194,0.089637,-0.264505,0.089637,0.584907,0.944744,0.570699,0.089637,0.089637,0.359837,0.000000])
#	arm.move_joint([0.000000,0.026180,-0.130900,-0.000000,-0.296706,-0.000000,0.261799,-0.300475,0.089637,-0.265758,0.089637,0.602857,1.014735,0.566233,0.089637,0.089637,0.411878,0.000000])
#	arm.move_joint([0.000000,0.010472,-0.115192,-0.000000,-0.293215,-0.000000,0.265290,-0.294774,0.089637,-0.267019,0.089637,0.614189,1.073089,0.561793,0.089637,0.089637,0.458900,0.000000])
#	arm.move_joint([0.000000,-0.005236,-0.099484,-0.000000,-0.289725,-0.000000,0.268781,-0.289164,0.089637,-0.268360,0.089637,0.619410,1.120698,0.557524,0.089637,0.089637,0.501287,0.000000])
#	arm.move_joint([0.000000,-0.020944,-0.083776,-0.000000,-0.286234,-0.000000,0.272271,-0.283719,0.089637,-0.269858,0.089637,0.618834,1.157998,0.553578,0.089637,0.089637,0.539164,0.000000])
#	arm.move_joint([0.000000,-0.036652,-0.068068,-0.000000,-0.282743,-0.000000,0.275762,-0.278517,0.089637,-0.271590,0.089637,0.612649,1.185111,0.550108,0.089637,0.089637,0.572462,0.000000])
#	arm.move_joint([0.000000,-0.052360,-0.052360,-0.000000,-0.279253,-0.000000,0.279253,-0.273636,0.089637,-0.273636,0.089637,0.600957,1.201914,0.547271,0.089637,0.089637,0.600957,0.000000])
#	arm.move_joint([0.000000,-0.068068,-0.036652,-0.000000,-0.275762,-0.000000,0.282743,-0.269152,0.089637,-0.276074,0.089637,0.583785,1.208073,0.545226,0.089637,0.089637,0.624288,0.000000])
#	arm.move_joint([0.000000,-0.083776,-0.020944,-0.000000,-0.272271,-0.000000,0.286234,-0.265144,0.089637,-0.278987,0.089637,0.561078,1.203038,0.544131,0.089637,0.089637,0.641960,0.000000])
#	arm.move_joint([0.000000,-0.099484,-0.005236,-0.000000,-0.268781,-0.000000,0.289725,-0.261688,0.089637,-0.282452,0.089637,0.532673,1.186008,0.544140,0.089637,0.089637,0.653335,0.000000])
#	arm.move_joint([0.000000,-0.115192,0.010472,-0.000000,-0.265290,-0.000000,0.293215,-0.258855,0.089637,-0.286546,0.089637,0.498251,1.155857,0.545401,0.089637,0.089637,0.657606,0.000000])
#	arm.move_joint([0.000000,-0.130900,0.026180,-0.000000,-0.261799,-0.000000,0.296706,-0.256713,0.089637,-0.291340,0.089637,0.457253,1.110983,0.548053,0.089637,0.089637,0.653730,0.000000])
#	arm.move_joint([0.000000,-0.146608,0.041888,-0.000000,-0.258309,-0.000000,0.300197,-0.255323,0.089637,-0.296901,0.089637,0.408725,1.049031,0.552224,0.089637,0.089637,0.640305,0.000000])
#	arm.move_joint([0.000000,-0.162316,0.057596,-0.000000,-0.254818,-0.000000,0.303687,-0.254738,0.089637,-0.303286,0.089637,0.351027,0.966318,0.558024,0.089637,0.089637,0.615291,0.000000])
#	arm.move_joint([0.000000,-0.178024,0.073304,-0.000000,-0.251327,-0.000000,0.307178,-0.255001,0.089637,-0.310547,0.089637,0.281157,0.856513,0.565548,0.089637,0.089637,0.575356,0.000000])
#	arm.move_joint([0.000000,-0.193732,0.089012,-0.000000,-0.247837,-0.000000,0.310669,-0.256147,0.089637,-0.318724,0.089637,0.192841,0.706823,0.574870,0.089637,0.089637,0.513981,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.258198,0.089637,-0.327847,0.089637,0.068107,0.481139,0.586045,0.089637,0.089637,0.413032,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.247934,0.080714,-0.331437,0.080714,0.076786,0.484716,0.579371,0.080714,0.080714,0.407930,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.237738,0.071779,-0.335073,0.071779,0.085552,0.488480,0.572811,0.071779,0.071779,0.402928,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.227612,0.062832,-0.338761,0.062832,0.094406,0.492431,0.566373,0.062832,0.062832,0.398025,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.217559,0.053875,-0.342504,0.053875,0.103349,0.496570,0.560063,0.053875,0.053875,0.393221,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.207581,0.044909,-0.346308,0.044909,0.112383,0.500897,0.553889,0.044909,0.044909,0.388514,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.197681,0.035936,-0.350176,0.035936,0.121507,0.505410,0.547857,0.035936,0.035936,0.383902,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.187861,0.026957,-0.354112,0.026957,0.130721,0.510106,0.541973,0.026957,0.026957,0.379385,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.178123,0.017974,-0.358122,0.017974,0.140025,0.514985,0.536245,0.017974,0.017974,0.374960,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.168469,0.008988,-0.362208,0.008988,0.149419,0.520042,0.530676,0.008988,0.008988,0.370623,0.000000])
#	arm.move_joint([0.000000,-0.209440,0.104720,-0.000000,-0.244346,-0.000000,0.314159,-0.158900,-0.000000,-0.366374,-0.000000,0.158900,0.525274,0.525274,-0.000000,-0.000000,0.366374,0.000000])



if __name__ == '__main__':
	rospy.init_node('trajectory_client')
	main()
print("Hello")
