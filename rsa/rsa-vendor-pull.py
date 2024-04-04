import requests
import csv

url = "https://platform.cloud.coveo.com/rest/search/v2?sitecoreItemUri=sitecore%3A%2F%2Fweb%2F%7B18754852-E1E0-4A88-8649-BA50991397CB%7D%3Flang%3Den%26amp%3Bver%3D1&siteName=RSAC-PROD-CD"

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2OCI6dHJ1ZSwidG9rZW5JZCI6InFoZG1tNndyazV3dWtsdW5uMnp0NjcyYndxIiwib3JnYW5pemF0aW9uIjoicnNhY3Byb2Q4bXlseTRraiIsInVzZXJJZHMiOlt7InR5cGUiOiJVc2VyIiwibmFtZSI6ImFub255bW91cyIsInByb3ZpZGVyIjoiRW1haWwgU2VjdXJpdHkgUHJvdmlkZXIifV0sInJvbGVzIjpbInF1ZXJ5RXhlY3V0b3IiXSwiaXNzIjoiU2VhcmNoQXBpIiwiZXhwIjoxNzEyMjY5OTQ2LCJpYXQiOjE3MTIxODM1NDZ9.HMqtqz4s9cSiNhplYcGEX1ml1viHvkvGkfPI8JNJcDw',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.rsaconference.com',
    'referer': 'https://www.rsaconference.com/search',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7',
    'referrer': 'https://www.rsaconference.com/marketplace/search',
    'numberOfResults': '100',
    'firstResult': '1',
    'excerptLength': '200',
    'siteName': 'RSAC-PROD-CD',
    'searchHub': 'Search',
    'pipeline': 'Global Site Search',
    'sortCriteria'  : 'relevancy',
    'tab'  : 'tab-all-results',
    'allowQueriesWithoutKeywords': 'true',
 }

data = {
    'actionsHistory': '[{"name":"Query","time":"2024-04-03T16:31:53.173Z"}]',
    'aq': "(@z95xtemplatename==Exhibitor) (((((((((((((((((@alltemplates==2204DA9DB19447FFBF5AF7C0EEC67835 OR @alltemplates==861A1192D20B412A8601AF8CF3EDF2FB) OR @alltemplates==617C862C21004E9E95E4D2E45C3AA199) OR @alltemplates==A0D81E7D92F04509B7AA4DC42D9AA03E) OR @alltemplates==797990ADE6CB4DAA98966F43D00C0A73) OR @alltemplates==55EC095E0EC649DBAA2B4AA11E4CC413) OR (@alltemplates==328837A4DFD54ECAB4221E77A186D28B (@z95xpath=D2E259F27BF340BB9A1C4FA776D1870D @z95xid<>D2E259F27BF340BB9A1C4FA776D1870D))) OR @alltemplates==8779545A8BED40E788D34C1EFDB71EA8) OR (@alltemplates==05391C07CCE8428BA18493AA80B0DE21 @advisoryz32xboard==1)) OR (@alltemplates==9C786508EB8847B2AE85C8E08369B8A4 ((@z95xpath=68F6938DF535413995A50E925A036DCF @z95xid<>68F6938DF535413995A50E925A036DCF) @showz32xinz32xmarketplace==True))) OR @alltemplates==3D0BF62F9C38468DB5FDFAD8924329E8) OR @ez120xpertblogreferencecount<>0) OR @ez120xpertsessionparticipantreferencecount<>0) OR @ez120xpertpodcastreferencecount<>0) OR @ez120xpertvideoreferencecount<>0) OR @ez120xpertwebcastreferencecount<>0) NOT @z95xtemplate==(ADB6CA4F03EF4F47B9AC9CE2BA53FF97,FE5DD82648C6436DB87A7C4210C7413B)))",
    'groupBy': "[{\"field\":\"@z95xtemplatename\",\"maximumNumberOfValues\":6,\"sortCriteria\":\"occurrences\",\"injectionDepth\":1000,\"completeFacetWithStandardValues\":true,\"allowedValues\":[\"Exhibitor\"],\"advancedQueryOverride\":\"((((((((((((((((@alltemplates==2204DA9DB19447FFBF5AF7C0EEC67835 OR @alltemplates==861A1192D20B412A8601AF8CF3EDF2FB) OR @alltemplates==617C862C21004E9E95E4D2E45C3AA199) OR @alltemplates==A0D81E7D92F04509B7AA4DC42D9AA03E) OR @alltemplates==797990ADE6CB4DAA98966F43D00C0A73) OR @alltemplates==55EC095E0EC649DBAA2B4AA11E4CC413) OR (@alltemplates==328837A4DFD54ECAB4221E77A186D28B (@z95xpath=D2E259F27BF340BB9A1C4FA776D1870D @z95xid<>D2E259F27BF340BB9A1C4FA776D1870D))) OR @alltemplates==8779545A8BED40E788D34C1EFDB71EA8) OR (@alltemplates==05391C07CCE8428BA18493AA80B0DE21 @advisoryz32xboard==1)) OR (@alltemplates==9C786508EB8847B2AE85C8E08369B8A4 ((@z95xpath=68F6938DF535413995A50E925A036DCF @z95xid<>68F6938DF535413995A50E925A036DCF) @showz32xinz32xmarketplace==True))) OR @alltemplates==3D0BF62F9C38468DB5FDFAD8924329E8) OR @ez120xpertblogreferencecount<>0) OR @ez120xpertsessionparticipantreferencecount<>0) OR @ez120xpertpodcastreferencecount<>0) OR @ez120xpertvideoreferencecount<>0) OR @ez120xpertwebcastreferencecount<>0) NOT @z95xtemplate==(ADB6CA4F03EF4F47B9AC9CE2BA53FF97,FE5DD82648C6436DB87A7C4210C7413B))\",\"constantQueryOverride\":\"(@z95xlanguage==en) (@z95xlatestversion==1) (@source==\\\"Coveo_web_index - NEW-PROD\\\")\"},{\"field\":\"@ez120xperttopics\",\"maximumNumberOfValues\":6,\"sortCriteria\":\"alphaascending\",\"injectionDepth\":1000,\"completeFacetWithStandardValues\":true,\"allowedValues\":[]},{\"field\":\"@industrytopicfullconference\",\"maximumNumberOfValues\":6,\"sortCriteria\":\"alphaascending\",\"injectionDepth\":1000,\"completeFacetWithStandardValues\":true,\"allowedValues\":[]},{\"field\":\"@industrytopicconferenceyear\",\"maximumNumberOfValues\":6,\"sortCriteria\":\"alphadescending\",\"injectionDepth\":1000,\"completeFacetWithStandardValues\":true,\"allowedValues\":[]}]",    
    # 'firstResult': '0',
    # 'numberOfResults': '100',
}

start = 0
page_size = 100
has_more_results = True

with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Vendor"])

    while has_more_results:
        data['firstResult'] = start
        data['numberOfResults'] = page_size

        response = requests.post(url, headers=headers, data=data)
        response_json = response.json()

        if 'totalCount' in response_json:
            print(response_json['totalCount'])
        else:
            print("No totalCount found in the response.")

        if 'results' in response_json:
            for result in response_json['results']:
                if 'title' in result:
                    print(result['title'])
                    writer.writerow([result['title']])
                else:
                    print("No title found in this result.")
            # Update start for the next page
            start += page_size
            # If the number of results is less than page_size, there are no more results
            if len(response_json['results']) < page_size:
                has_more_results = False
        else:
            print("No results found in the response.")
            has_more_results = False

file.close()