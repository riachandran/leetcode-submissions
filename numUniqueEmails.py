class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = []
        for email in emails:
            local,domain = email.split('@')
            local = local.replace(".", "").split('+')[0]
            finalemail = local+'@'+domain
            if finalemail not in uniqueEmails: uniqueEmails.append(finalemail)
        return len(uniqueEmails)
