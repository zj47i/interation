#!/usr/bin/env python3
"""
텔레그램 봇 메시지 수신기
Telegram Bot Message Receiver

이 스크립트는 텔레그램 봇으로부터 메시지를 받는 기본적인 기능을 제공합니다.
This script provides basic functionality to receive messages from a Telegram bot.
"""

import logging
import os
from typing import Optional

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

# 로깅 설정
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self, token: Optional[str] = None):
        """텔레그램 봇 초기화
        
        Args:
            token: 봇 토큰. None일 경우 환경변수에서 가져옴
        """
        self.token = token or os.getenv('TELEGRAM_BOT_TOKEN')
        if not self.token:
            raise ValueError("봇 토큰이 필요합니다. .env 파일에 TELEGRAM_BOT_TOKEN을 설정하거나 token 매개변수를 제공하세요.")
        
        self.application = Application.builder().token(self.token).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """메시지 핸들러 설정"""
        # 명령어 핸들러
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        
        # 텍스트 메시지 핸들러
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        # 에러 핸들러
        self.application.add_error_handler(self.error_handler)
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """'/start' 명령어 처리"""
        user = update.effective_user
        await update.message.reply_html(
            f"안녕하세요 {user.mention_html()}님!\n"
            f"저는 메시지를 받는 텔레그램 봇입니다.\n"
            f"/help 명령어로 도움말을 확인하세요."
        )
        logger.info(f"User {user.id} ({user.username}) started the bot")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """'/help' 명령어 처리"""
        help_text = """
사용 가능한 명령어:
/start - 봇 시작
/help - 도움말 보기

메시지를 보내시면 봇이 받은 메시지를 확인해드립니다.
        """
        await update.message.reply_text(help_text)
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """일반 텍스트 메시지 처리"""
        user = update.effective_user
        message_text = update.message.text
        
        # 받은 메시지 로깅
        logger.info(f"Received message from {user.id} ({user.username}): {message_text}")
        
        # 메시지 확인 응답
        response = f"메시지를 받았습니다: '{message_text}'"
        await update.message.reply_text(response)
    
    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE):
        """에러 처리"""
        logger.error(f"Exception while handling an update: {context.error}")
    
    def start_polling(self):
        """봇 실행 (폴링 방식)"""
        logger.info("봇이 시작되었습니다. 메시지를 기다리는 중...")
        print("봇이 시작되었습니다. 종료하려면 Ctrl+C를 누르세요.")
        
        try:
            self.application.run_polling(allowed_updates=Update.ALL_TYPES)
        except KeyboardInterrupt:
            logger.info("봇이 종료되었습니다.")
            print("봇이 종료되었습니다.")


def main():
    """메인 함수"""
    try:
        bot = TelegramBot()
        bot.start_polling()
    except ValueError as e:
        print(f"설정 오류: {e}")
        print("사용법:")
        print("1. .env 파일을 생성하고 TELEGRAM_BOT_TOKEN=your_bot_token_here 를 추가하세요")
        print("2. 또는 환경변수 TELEGRAM_BOT_TOKEN을 설정하세요")
    except Exception as e:
        logger.error(f"예기치 않은 오류: {e}")
        print(f"오류가 발생했습니다: {e}")


if __name__ == '__main__':
    main()