FROM python:3
ADD bot.py /
ADD Dice.py /
ADD token.txt /
RUN pip install discord
CMD ["python", "./bot.py"]