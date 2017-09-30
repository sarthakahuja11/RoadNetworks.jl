
//#include <ros/ros.h>
//#include <pcl_ros/point_cloud.h>
//#include <pcl/point_types.h>
//#include <boost/foreach.hpp>

#include "subscribe_pcl.hpp"

typedef pcl::PointCloud<pcl::PointXYZ> PointCloud;

void callback(const PointCloud::ConstPtr& msg)
{
  printf ("Cloud: width = %d, height = %d\n", msg->width, msg->height);
  BOOST_FOREACH (const pcl::PointXYZ& pt, msg->points)
    printf ("\t(%f, %f, %f)\n", pt.x, pt.y, pt.z);
}

int main(int argc, char** argv)
{
	  ros::init(argc, argv, "sub_pcl");
	  ros::NodeHandle nh;
	  ros::Publisher pub = nh.advertise<PointCloud> ("points", 1);
          PointCloud::Ptr msg(new PointCloud);
	  msg->header.frame_id = "Sensor";
          ros::Rate loop_rate(20);
          tf::Transform transform;
          static tf::TransformBroadcaster br;
	  //pcl::PointXYZ& point;
		while(ros::ok())
		{
			pcl::PointXYZ(1.0, 2.0, 3.0);
			transform.setOrigin(tf::Vector3(5.0,6.0,0.0));  //(goalx, goaly, 0.0) );
			tf::Quaternion q;
			q.setRPY(0, 0, 0);
			transform.setRotation(q);
			br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "Sensor", "Sign"));
			pub.publish(msg);
			ros::spinOnce();
			loop_rate.sleep ();
		}	 

}