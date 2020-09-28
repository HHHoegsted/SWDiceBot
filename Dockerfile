FROM python:3
ADD bot.py /
ADD Dice.py /
RUN pip install discord
CMD ["python", "./bot.py"]
