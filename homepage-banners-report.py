from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from render_pdf import render_pdf


def get_context():
    date = datetime.today().strftime("%A, %d %B %Y")
    return {
        "date": date,
        "overall": {
            "metrics": {
                "impressions": 6000,
                "clicks": 500,
                "ctr": 0.08,
                "orders": 10,
                "gmv": 2500,
                "cvr": 2,
            },
        },
        "data": [
            {
                "imgSrc": "https://cdn.sanity.io/images/p4af87yj/production/26e605ed6d89a3d0899a2baf9da80896340a9594-627x836.jpg?w=200&dpr=3&fm=webp&q=75",
                "metrics": {
                    "impressions": 2000,
                    "clicks": 100,
                    "ctr": 0.05,
                    "orders": 10,
                    "gmv": 1000,
                    "cvr": 2,
                },
            },
            {
                "imgSrc": "https://cdn.sanity.io/images/p4af87yj/production/3928855790199c6b4c37483e80af74118547f85a-632x316.jpg?w=350&dpr=3&fm=webp&q=75",
                "metrics": {
                    "impressions": 4000,
                    "clicks": 400,
                    "ctr": 0.1,
                    "orders": 15,
                    "gmv": 1500,
                    "cvr": 3,
                },
            },
        ],
    }


def run():
    env = Environment(
        loader=FileSystemLoader("templates"), autoescape=select_autoescape()
    )
    template = env.get_template("report-template.html")
    with open("report.html", "w", encoding="utf-8") as f:
        chars_written = f.write(template.render(get_context()))
        print("chars_written", chars_written)

    render_pdf()
    print("PDF rendered")


if __name__ == "__main__":
    run()
