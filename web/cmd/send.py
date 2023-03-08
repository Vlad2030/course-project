import subprocess


class Methods:
    def __init__(self: any, command: str, stdout: bool) -> None:
        if stdout:
            self.stdout = subprocess.PIPE
        else:
            self.stdout = False

        self.command = command

    def send(command: str, stdout: bool = False) -> None:
        if command:
            if stdout:
                return subprocess.run(
                    args=command.split(" "),
                    stdout=subprocess.PIPE,
                ).stdout.decode("utf-8")

            elif stdout is False:
                return subprocess.run(
                    args=command.split(" "),
                    stdout=None,
                )

            else:
                raise ValueError

        else:
            raise ValueError
