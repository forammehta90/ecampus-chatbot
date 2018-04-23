import os
import time
from slackclient import SlackClient
from controller import controller


AT_BOT = os.environ["bot_id"]
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
control=controller()

def handle_command(command, channel):
    slack_client.api_call("chat.postMessage", channel=channel, text=control.find_solution(command), as_user=True)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            print (output,"out")
            if output and 'text' in output and output['user'].strip() != AT_BOT:
                print (output['user'].strip(),"user",AT_BOT)
                return output['text'].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1     
    if slack_client.rtm_connect():
        print ("SpartanBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            print (command,channel)
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
	    print ("Connection failed. Invalid Slack token or bot ID?")