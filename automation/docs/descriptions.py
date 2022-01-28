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
                f'<li><b>{key}</b>:<xmp>{value}</xmp></li>'
            )
        return description.format(values=values)
