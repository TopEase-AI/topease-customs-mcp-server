import asyncio
from topease_mcp.customs import CustomsDataService, CustomsQueryParams, TradeType

async def test():
    svc = CustomsDataService()

    # Test 1: No filters, raw mock
    params = CustomsQueryParams(page=1, page_size=5)
    records = svc._generate_mock_records(params)
    print('Total raw records:', len(records))
    for r in records[:5]:
        prodesc = r.prodesc[:30] if r.prodesc else '(empty)'
        print(f'  ie={r.ie}, hs={r.hs_code}, prodesc={prodesc}, importer_tcode={r.importer_tcode}, origin={r.origin_country}')

    # Test 2: TCode filter
    params2 = CustomsQueryParams(tcode='IMPORTER_0001', page=1, page_size=3)
    result2 = await svc.search(params2)
    print('\nTCode search (IMPORTER_0001): total=%d' % result2.total)
    for r in result2.records:
        print(f'  {r.importer_name} | {r.hs_code} | {r.trade_type}')

    # Test 3: Product keyword
    params3 = CustomsQueryParams(product_keyword='CABIN', page=1, page_size=3)
    result3 = await svc.search(params3)
    print('\nProduct search (CABIN): total=%d' % result3.total)
    for r in result3.records:
        print(f'  {r.prodesc} | {r.hs_code}')

    # Test 4: HS code
    params4 = CustomsQueryParams(hs_code='8415', page=1, page_size=3)
    result4 = await svc.search(params4)
    print('\nHS code (8415): total=%d' % result4.total)
    for r in result4.records:
        print(f'  {r.hs_code} | {r.prodesc}')

    # Test 5: Country
    params5 = CustomsQueryParams(country='Japan', page=1, page_size=3)
    result5 = await svc.search(params5)
    print('\nCountry=Japan: total=%d' % result5.total)
    for r in result5.records:
        print(f'  {r.origin_country} | {r.hs_code}')

    # Test 6: No filter at all via search
    params6 = CustomsQueryParams(page=1, page_size=3)
    result6 = await svc.search(params6)
    print('\nNo filter: total=%d' % result6.total)
    for r in result6.records:
        print(f'  {r.importer_name} | {r.hs_code} | {r.trade_type}')

asyncio.run(test())
