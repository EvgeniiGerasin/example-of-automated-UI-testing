class BaseDescription:

    @staticmethod
    def create(data: dict) -> str:
        description = (
            '<ul>'
            '{values}'
            '</ul>'
        )
        values = ''
        for key, value in data.items():
            values += (
                f'<li><b>{key}</b>: {value}</li>'
            )
        return description.format(values=values)
