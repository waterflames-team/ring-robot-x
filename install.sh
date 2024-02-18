#!/bin/bash
echo ----------------------------------
echo RingRobotX Installer
echo Powered by Lingkong Team
echo ----------------------------------

function log_info() {
  echo -e "\033[32;40m[INFO] $1 \033[0m"
}

function log_error() {
  echo -e "\033[31;40m[ERROR] $1 \033[0m"
}

function log_warn() {
  echo -e "\033[33;40m[WARN] $1 \033[0m"
}

function error_dump() {
  log_error "$1"
  exit 1
}

function check_program() {
  log_info "Checking for $1 ..."

  local installed='0'
  path=$(command -v "$1") || { local installed='1'; }
  # fail on non-zero return value
  if [ "$installed" -ne 0 ]; then
    error_dump "$1: command not found."
  fi
  log_info "Checking for $1 ... $path"
}

function install_system_pkgs() {
  log_info "Installing system requirements ..."
  sudo apt-get update || error_dump "install_system_pkgs - apt-get update error"
  sudo apt-get install python3 python3-pip git python3-pyaudio swig libatlas-base-dev pulseaudio make alsa-utils sox libsox-fmt-mp3
  log_info "Installing system requirements ... Done"
}

function install_snowboy() {
  log_info "Installing requirement: 'snowboy' ..."
  if [ -d "snowboy" ]; then
    log_info "Snowboy already installed."
    return
  fi
  git clone https://gitee.com/zhetengtiao/snowboy.git || error_dump "install_snowboy - git clone error"
  cd snowboy/swig/Python3 || error_dump "install_snowboy - cd error"
  make || error_dump "install_snowboy - snowboy making error"
  cd ../../../
  log_info "Installing requirement: 'snowboy' ... Done"
}

function install_ringrobotx() {
  log_info "Installing RingRobotX ..."
  if [ -d "ring-robot-x" ]; then
    log_info "RingRobotX already installed."
    return
  fi
  git clone https://gitee.com/waterflames-team/ring-robot-x.git -b develop || error_dump "install_ringrobotx - git clone error"
  cp snowboy/swig/Python3/_snowboydetect.so ring-robot-x/func_packages/ZZZ_Snowboy || error_dump "install_ringrobotx - copy so error"
  cp snowboy/examples/Python3/snowboydecoder.py ring-robot-x/func_packages/Snowboy || error_dump "install_ringrobotx - copy decoder error"
  cp snowboy/examples/Python3/snowboydetect.py ring-robot-x/func_packages/ZZZ_Snowboy || error_dump "install_ringrobotx - copy detect error"
  cp -a snowboy/resources/ ring-robot-x/func_packages/ZZZ_Snowboy/resources || error_dump "install_ringrobotx - copy res error"
  chmod 0777 ../ringrobotx/ -R || error_dump "install_ringrobotx - chmod error"
  cd ring-robot-x || error_dump "install_ringrobotx - cd error"
  if [ "$BREAK_SYSTEM_PACKAGES" -eq 1 ]; then
    pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package || error_dump "Install Python requirements - Cannot install package"
  else
    pip3 install -r requirements.txt --break-system-packages -i https://pypi.tuna.tsinghua.edu.cn/simple some-package || error_dump "Install Python requirements - Cannot install package"
  fi
  python3 ring.py --firstload || error_dump "install_ringrobotx - firstload error"
  log_info "Installing RingRobotX ... Done"
}

function pre_install() {
  mkdir -p ringrobotx
  cd ringrobotx || error_dump "pre_install - cd error"
}

function is_venv() {
  if [ -z "$VIRTUAL_ENV" ]; then
    return 1
  else
    return 0
  fi

}

function is_debian()
{
  if [ -f "/etc/os-release" ]; then
    if grep -q "debian" "/etc/os-release"; then
      return 0
    fi
  fi
  return 1
}

function main() {
  declare BREAK_SYSTEM_PACKAGES=0
  if is_debian; then
    if is_venv; then
      log_info "Running in venv."
    else
      log_warn "Cannot install pip packages on Debian, please use venv."
      log_warn "We will install by passing '--break-system-packages'."
      log_warn "Please make sure you know what you are doing."
      echo "Press any key to continue, or press Ctrl+C to cancel."
      read -n 1 -s -r
      BREAK_SYSTEM_PACKAGES=1
    fi
  fi

  install_system_pkgs

  check_program "git"
  check_program "make"
  check_program "chmod"
  check_program "pip3"
  check_program "python3"
  check_program "apt-get"
  check_program "swig"

  pre_install
  install_snowboy
  install_ringrobotx
  log_info "RingRobotX Ready."
  exit
}

main
