class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            tokens = email.split('@')
            if len(tokens) > 2:
                continue
            else:
                local, domain = tokens[0], tokens[1]
                local = local.replace('.', '')
                plus_index = local.find('+')
                if plus_index != -1:
                    local = local[:plus_index]
                email = local + '@' + domain
                unique_emails.add(email)
        return len(unique_emails)
        
