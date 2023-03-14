from flask import Flask, render_template

from db.services import OperationDB
from db.connection import session

from loguru import logger


app = Flask(__name__)


@app.route('/')
def index():
    service = OperationDB(session=session)
    records = service.get_all_records()

    total_sum = sum(int(record.price_dollar) for record in records)        # Сумма всех заказов
    sorted_record_by_date = sorted(records, key=lambda x: x.delivery_date)
    data = [record.price_dollar for record in records]                     # Список суммы заказов
    labels = [record.delivery_date.strftime('%d-%m-%Y') for record in sorted_record_by_date]  # Сортированный список дат

    return render_template('index.html',
                           records=records,
                           total_sum=total_sum,
                           data=data,
                           labels=labels)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
