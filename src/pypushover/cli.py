import click
import os
from .pushover import send_message

@click.group()
def cli():
    """Pypushover CLI for sending notifications."""
    pass

@cli.command()
@click.argument('message', required=False, default='Your code has finished running!')
@click.option('--title', default=None, help='Optional title for the message')
@click.option('--device', default=None, help='Optional specific device to send to')
@click.option('--priority', default=0, type=int, help='Message priority (-1 to 2)')
def show(message, title, device, priority):
    """
    Send a message via Pushover.
    
    Sends a notification with the specified message and optional parameters.
    
    Args:
        message: The message text to send
        title: Optional title for the message
        device: Optional specific device to send to
        priority: Message priority (-1 to 2)
    """
    try:
        # Filter out None values to prevent unexpected keyword arguments
        if not title:
            # set to current working directory
            title = os.getcwd().split("/")[-1]

        kwargs = {
            'message': message,
            **(({'title': title} if title else {})),
            **(({'device': device} if device else {})),
            **(({'priority': priority} if priority != 0 else {}))
        }
        
        result = send_message(**kwargs)
        click.echo(f"Message sent successfully.")
    except Exception as e:
        click.echo(f"Error sending message: {e}", err=True)
        exit(1)

def main():
    cli()

if __name__ == '__main__':
    main()