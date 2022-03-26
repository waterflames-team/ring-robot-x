#!/bin/bash
echo ----------------------------------
echo        RingRobotX Installer
echo      Powered by Lingkong Team
echo ----------------------------------

if [ $UID -ne 0 ] ; then
	echo -e "\033[33;40m[Warning] APT need root running! The script will run as sudo. \033[0m"
	echo -e ""
	read -r -p "\033[33;40m[Warning] Are you sure? (Y,N)\033[0m" input
  case $input in
      [yY][eE][sS]|[yY])
      echo -e "\033[33;40m[Warning] Continue......\033[0m"
      ;;
      [nN][oO]|[nN])
      exit 1
          ;;
      *)
      echo -e "\033[33;40m[Warning] Invalid input\033[0m"
      exit 1
      ;;
  esac
fi

function check_apt(){
  local apt='0'
  command -v $1 >/dev/null 2>&1 || { local apt='1'; }

  # fail on non-zero return value
  if [ "$apt" -ne 0 ]; then
      echo -e "\033[31;40m[ERROR] apt command NOT found \033[0m"
      exit 1
  fi
}

function error_dump(){
  echo -e "\033[31;40m[ERROR] $1 \033[0m"
  exit 1
}

function install_snowboy(){
  echo -e "\033[32;40m[INFO] Installing snowboy requires......\033[0m"
  git clone https://github.com/Kitt-AI/snowboy.git || error_dump "install_snowboy - git clone error"
  cd snowboy/swig/Python3 || error_dump "install_snowboy - cd error"
  make || error_dump "install_snowboy - snowboy making error"
  echo -e "\033[32;40m[INFO] Success! \033[0m"
  cd ../../../
}

function install_ringrobotx(){
  echo -e "\033[32;40m[INFO] Installing RingRobotX......\033[0m"
  git clone https://github.com/lkteam/ring-robot-x.git || error_dump "install_ringrobotx - git clone error"
  cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/model || error_dump "install_ringrobotx - copy error"
  cp snowboy/examples/Python3/snowboydecoder.py ring-robot-x/model || error_dump "install_ringrobotx - copy error"
  cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/model || error_dump "install_ringrobotx - copy error"
}

function install_before_require(){
  require=(python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils)
  echo -e "\033[32;40m[INFO] Installing requires......\033[0m"
  for i in ${require[*]}
  do
    sudo apt install ${i} -y || error_dump "install_before_require - Cannot install package:${i}"
  done
  echo -e "\033[32;40m[INFO] apt install Success! \033[0m"
  require=(pydub playsound)
  for i in ${require[*]}
  do
    sudo pip3 install ${i} -i https://pypi.tuna.tsinghua.edu.cn/simple some-package || error_dump "install_before_require - Cannot install package:${i}"
  done
  echo -e "\033[32;40m[INFO] Success! \033[0m"
}

function before_install(){
  mkdir ~/ringrobotx
  cd ~/ringrobotx || error_dump "before_install - cd error"
}

function main(){
  check_apt "apt"
  before_install
  install_before_require
  install_snowboy
  install_ringrobotx
  echo -e "\033[32;40m[INFO] RingRobotX Ready! \033[0m"
  echo -e "\033[32;40m[INFO] Next, you need to copy the snowboy model to ~/ringrobotx/assets/snowboy/model.pmdl , see RingRoxotX Wiki \033[0m"
  exit
}

main