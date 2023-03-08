import platform
import distro
import cmd.send
from userdata import file

user_platform: str = platform.system()
user_distro: str = distro.like()
webapp_version: str = file.read(destigation="./version")

while __name__ == "__main__":
    print(
        f"""
Test WebApp Setup\t{webapp_version}
Run Test WebApp \t(1)
Install dependencies\t(2)
Build Docker Image\t(3)
"""
    )
    value: str = input("Number: ")
    if value:
        if "1" in value:
            if "Windows" or "Darwin" in user_platform:
                cmd.send.Methods.send(command="python main.py")

            if "Linux" in user_platform:
                cmd.send.Methods.send(command="python3 main.py")

        elif "2" in value:
            if "Windows" or "Darwin" in user_platform:
                cmd.send.Methods.send(command="pip install -r requirements.txt")

            if "Linux" in user_platform:
                cmd.send.Methods.send(command="pip install -r requirements.txt")

        elif "3" in value:
            if "Windows" in user_platform:
                pass

            if "Linux" or "Darwin" in user_platform:
                docker_path: str = cmd.send.Methods.send(
                    command="whereis docker",
                    stdout=True,
                )
                if "/etc/bin/" in docker_path:
                    cmd.send.Methods.send(command="docker build -t webapp")
