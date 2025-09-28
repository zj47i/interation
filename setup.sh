#!/bin/bash

# 가상환경 설정 및 프로젝트 초기화 스크립트
# Virtual Environment Setup and Project Initialization Script

echo "=== 텔레그램 봇 프로젝트 설정 ==="
echo "=== Telegram Bot Project Setup ==="

# Python 버전 확인
python3 --version
if [ $? -ne 0 ]; then
    echo "오류: Python 3가 설치되어 있지 않습니다."
    echo "Error: Python 3 is not installed."
    exit 1
fi

# 가상환경 생성
echo "가상환경 생성 중... (Creating virtual environment...)"
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "오류: 가상환경 생성에 실패했습니다."
    echo "Error: Failed to create virtual environment."
    exit 1
fi

# 가상환경 활성화
echo "가상환경 활성화 중... (Activating virtual environment...)"
source venv/bin/activate

# pip 업그레이드
echo "pip 업그레이드 중... (Upgrading pip...)"
pip install --upgrade pip

# 필요한 패키지 설치
echo "필요한 패키지 설치 중... (Installing required packages...)"
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "오류: 패키지 설치에 실패했습니다."
    echo "Error: Failed to install packages."
    exit 1
fi

# .env 파일 설정
if [ ! -f ".env" ]; then
    echo ".env 파일 생성 중... (Creating .env file...)"
    cp .env.example .env
    echo ""
    echo "중요: .env 파일에서 TELEGRAM_BOT_TOKEN을 설정해주세요!"
    echo "Important: Please set TELEGRAM_BOT_TOKEN in the .env file!"
    echo ""
fi

echo "=== 설정 완료! ==="
echo "=== Setup Complete! ==="
echo ""
echo "다음 단계:"
echo "Next steps:"
echo "1. .env 파일을 편집하여 봇 토큰을 설정하세요"
echo "   Edit .env file and set your bot token"
echo "2. 가상환경을 활성화하세요: source venv/bin/activate"
echo "   Activate virtual environment: source venv/bin/activate"
echo "3. 봇을 실행하세요: python telegram_bot.py"
echo "   Run the bot: python telegram_bot.py"