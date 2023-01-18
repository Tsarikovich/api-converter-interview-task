import json

import aiohttp


class XEParser:
    base_convert_url = 'https://www.xe.com/currencyconverter/convert/'

    @staticmethod
    async def get_page(url: str) -> str | None:
        """
        Getting html code by url
        :return html text
        """

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()

        return None

    @staticmethod
    async def convert(amount: float, from_: str, to_: str) -> float:
        """
        Parsing converted value by amount, from and to currencies
        :return converted value
        """

        params = f'?Amount={amount}&From={from_}&To={to_}'
        html = await XEParser.get_page(XEParser.base_convert_url + params)
        return XEParser.extract_converted_value(html)

    @staticmethod
    def extract_converted_value(html: str) -> float:
        """
        Extracting needed value from html code
        :return converted value
        """

        start = html.rfind('result__BigRate-sc')
        while html[start] != '>':
            start += 1

        end = start
        while html[end] != '<':
            end += 1

        str_result = html[start + 1: end].replace(',', '')
        return float(str_result)

    @staticmethod
    def extract_currencies(html: str) -> dict:
        """
        Extracting currencies from html code
        :return dict of currencies names: currency codes
        """

        start = html.rfind('type="application/json">') + len(
            'type="application/json">'
        )
        end = html.rfind('</script>')

        json_str = html[start:end]
        currencies_dict = json.loads(json_str)['props']['pageProps'][
            'commonI18nResources'
        ]['currencies']['en']
        currencies_names = {
            currencies_dict[currency]['name']: currency
            for currency in currencies_dict
        }

        return currencies_names

    @staticmethod
    async def get_currencies() -> dict:
        """
        Parsing currencies from xe.com
        :return dict of currencies names: currency codes
        """

        html = await XEParser.get_page(XEParser.base_convert_url)
        currencies = XEParser.extract_currencies(html)
        return currencies
