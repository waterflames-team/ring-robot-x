#!/bin/bash
echo ----------------------------------
echo RingRobotX Installer
echo Powered by Lingkong Team
echo ----------------------------------

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
  git clone https://gitee.com/zhetengtiao/snowboy.git || error_dump "install_snowboy - git clone error"
  cd snowboy/swig/Python3 || error_dump "install_snowboy - cd error"
  make || error_dump "install_snowboy - snowboy making error"
  echo -e "\033[32;40m[INFO] Success! \033[0m"
  cd ../../../
}

function install_ringrobotx(){
  echo -e "\033[32;40m[INFO] Installing RingRobotX......\033[0m"
  git clone https://gitee.com/waterflames-team/ring-robot-x.git -b develop || error_dump "install_ringrobotx - git clone error"
  cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/func_packages/ZZZ_Snowboy || error_dump "install_ringrobotx - copy so error"
  cp snowboy/examples/Python3/snowboydecoder.py ring-robot-x/func_packages/Snowboy || error_dump "install_ringrobotx - copy decoder error"
  cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/func_packages/ZZZ_Snowboy || error_dump "install_ringrobotx - copy detect error"
  cp -a snowboy/resources/ ring-robot-x/func_packages/ZZZ_Snowboy/resources || error_dump "install_ringrobotx - copy res error"
  chmod 777 ../ringrobotx/ -R || error_dump "install_ringrobotx - chmod error"
  cd ring-robot-x || error_dump "install_ringrobotx - cd error"
  sudo pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package || error_dump "install_before_require - Cannot install package"
  python3 ring.py --firstload || error_dump "install_ringrobotx - firstload error"
}

function install_before_require(){
  require=(python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils sox libsox-fmt-mp3)
  echo -e "\033[32;40m[INFO] Installing requires......\033[0m"
  for i in ${require[*]}
  do
    sudo apt install ${i} -y || error_dump "install_before_require - Cannot install package:${i}"
  done
  echo -e "\033[32;40m[INFO] apt install Success! \033[0m"
  echo -e "\033[32;40m[INFO] Success! \033[0m"
}

function before_install(){
  mkdir ringrobotx
  cd ringrobotx || error_dump "before_install - cd error"
}

function main(){
  check_apt "apt"
  before_install
  install_before_require
  install_ringrobotx
  echo -e "\033[32;40m[INFO] RingRobotX Ready! \033[0m"
  exit
}

main