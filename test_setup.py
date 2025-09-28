#!/usr/bin/env python3
"""
텔레그램 봇 테스트 스크립트
Telegram Bot Test Script

실제 봇 토큰 없이 봇 구조를 테스트합니다.
Tests the bot structure without requiring an actual bot token.
"""

import sys
import os

# 현재 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """필요한 모듈들이 제대로 임포트되는지 테스트"""
    print("테스트: 모듈 임포트...")
    try:
        from telegram_bot import TelegramBot
        print("✓ TelegramBot 클래스 임포트 성공")
        
        import telegram
        print("✓ python-telegram-bot 라이브러리 임포트 성공")
        
        from dotenv import load_dotenv
        print("✓ python-dotenv 라이브러리 임포트 성공")
        
        return True
    except ImportError as e:
        print(f"✗ 임포트 실패: {e}")
        return False

def test_bot_initialization():
    """봇 초기화 테스트 (토큰 없이)"""
    print("\n테스트: 봇 초기화...")
    try:
        from telegram_bot import TelegramBot
        
        # 토큰 없이 초기화 시도 (예외가 발생해야 함)
        try:
            bot = TelegramBot()
            print("✗ 토큰 없이 봇이 생성됨 (예상되지 않은 동작)")
            return False
        except ValueError as e:
            print(f"✓ 토큰 없이 초기화 시 올바른 예외 발생: {e}")
            return True
    except Exception as e:
        print(f"✗ 예기치 않은 오류: {e}")
        return False

def test_file_structure():
    """프로젝트 파일 구조 테스트"""
    print("\n테스트: 파일 구조...")
    required_files = [
        'telegram_bot.py',
        'requirements.txt', 
        '.env.example',
        'setup.sh',
        'README.md',
        '.gitignore'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✓ {file} 존재")
    
    if missing_files:
        print(f"✗ 누락된 파일들: {missing_files}")
        return False
    
    print("✓ 모든 필수 파일이 존재함")
    return True

def main():
    """메인 테스트 함수"""
    print("=== 텔레그램 봇 프로젝트 테스트 ===")
    print("=== Telegram Bot Project Test ===\n")
    
    tests = [
        ("파일 구조", test_file_structure),
        ("모듈 임포트", test_imports),
        ("봇 초기화", test_bot_initialization),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} 테스트 ---")
        if test_func():
            passed += 1
            print(f"✓ {test_name} 테스트 통과")
        else:
            print(f"✗ {test_name} 테스트 실패")
    
    print(f"\n=== 테스트 결과 ===")
    print(f"통과: {passed}/{total}")
    
    if passed == total:
        print("✓ 모든 테스트 통과! 봇 기본 구조가 올바르게 설정되었습니다.")
        return True
    else:
        print("✗ 일부 테스트가 실패했습니다.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)