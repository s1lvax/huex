import argparse
from .light_controller import LightController
from .conbee import Conbee

def main():
    parser = argparse.ArgumentParser(description="Huex CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for 'show' command
    parser_show = subparsers.add_parser('show', help='Show all lights')

    # Subparser for 'control' command
    parser_control = subparsers.add_parser('control', help='Control a specific light')
    parser_control.add_argument('light_id', type=int, help='ID of the light to control')
    parser_control.add_argument('action', choices=['on', 'off'], help='Action to perform on the light')

    args = parser.parse_args()

    # Initialize Conbee and LightController
    conbee = Conbee()
    light_controller = LightController(conbee)

    # Execute commands based on parsed arguments
    if args.command == 'show':
        light_controller.show_all_lights()
    elif args.command == 'control':
        light_controller.control_light(args.light_id, args.action)

if __name__ == "__main__":
    main()
