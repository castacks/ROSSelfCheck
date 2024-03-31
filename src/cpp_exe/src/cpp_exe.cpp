
#include <memory>

#include <rclcpp/rclcpp.hpp>

// TODO: properly include the cpp_exe_class.hpp.

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<CounterSubsriber>());
    rclcpp::shutdown();
    return 0;
}
