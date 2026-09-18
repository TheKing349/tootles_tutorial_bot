from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PathSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterFile

def generate_launch_description():

    # Calculates the map to odom transform
    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathSubstitution(FindPackageShare("slam_toolbox")), "/launch/online_async_launch.py"]
        ),
        launch_arguments={'use_sim_time': 'true'}.items(),
    )
    
    # Launches the navigation stack (planner, controller, behavior trees)
    nav2_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathSubstitution(FindPackageShare("nav2_bringup")), "/launch/navigation_launch.py"]
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'params_file': [PathSubstitution(FindPackageShare("bringup")), "/config/nav2_params.yaml"]
        }.items(),
    )

    return LaunchDescription(
        [
            slam_toolbox,
            nav2_bringup
        ]
    )
