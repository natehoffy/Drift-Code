import React, { Component } from 'react'
import { fetchEloquaEnrichment } from 'app/modules/contactSidebar/api/integrations'
import { Button } from '@driftt/tide-core'
import { DefaultPlaceholder } from '../ExpandedChatSidebar/PlaceholderCards'
import { isNil, equals, pathOr, isEmpty } from 'ramda'
import EloquaIcon from 'images/eloqua'
import Card from 'components/ContactSidebar/Cards/Card'
import EnrichmentError from 'components/ContactSidebar/ErrorStates/EnrichmentError'
import withTracking from 'components/hocs/withTracking'

const defaultState = {
  contactData: null,
  hasNoData: true,
  firstLoad: false
}

const SURF_BASE_URL = 'http://surf.service-now.com/mktdriftleadredirect.do'
const SN_ORG_ID = 110874

class EloquaCard extends Component {
  constructor(props) {
    super(props)

    this.state = {
      contactData: null,
      firstLoad: true,
      hasNoData: false
    }
  }
  componentDidMount() {
    this.getEloquaDetails()
  }

  componentDidUpdate(prevProps) {
    if (!equals(this.props.email, prevProps.email)) {
      // eslint-disable-next-line react/no-did-update-set-state
      this.setState({
        firstLoad: true
      }, this.getEloquaDetails)
    }
  }

  generateSurfLink() {
    const { driftContact, email } = this.props

    const bu = pathOr('', ['attributes', 'product_bu'], driftContact) || ''
    const fn = pathOr('', ['attributes', 'first_name'], driftContact) || ''
    const ln = pathOr('', ['attributes', 'last_name'], driftContact) || ''
    const country = pathOr('', ['attributes', 'country'], driftContact) || ''
    const state = pathOr('', ['attributes', 'state'], driftContact) || ''
    const company = pathOr('', ['attributes', 'company'], driftContact) || ''
    const phone = pathOr('', ['phone'], driftContact)
    const cid = 16825 // fixed by servicenow

    return encodeURI(`${SURF_BASE_URL}?cid=${cid}&bu=${bu}&em=${email}&fn=${fn}&ln=${ln}&ctry=${country}&st=${state}&co=${company}&ph=${phone}`)
  }

  getEloquaDetails = async () => {
    const { email } = this.props

    if (isNil(email)) {
      this.setState(defaultState)

      return
    }

    try {
      const { data: eloquaData } = await fetchEloquaEnrichment(email)

      this.setState({
        contactData: eloquaData,
        firstLoad: false,
        hasNoData: false
      })
    } catch(e) {
      console.warn(e)

      this.setState(defaultState)
    }
  }

  render() {
    const { contactData, firstLoad, hasNoData } = this.state
    const { email, currentUser } = this.props

    const showSurfButton = email && currentUser && (currentUser.orgId === SN_ORG_ID || currentUser.orgId === 1)

    if (isNil(contactData) && firstLoad) {
      return (
        <div>
          <DefaultPlaceholder index={1} />
        </div>
      )
    }

    return (
      <Card
        title="Eloqua Details"
        hasSettings={false}
        cornerIcon={EloquaIcon}
        iconWidth={20}
        iconHeight={15}
      >
        {((!isNil(contactData) && !isEmpty(contactData)) && !isNil(email)) &&
            <div>
              <div className="field-row">
                <div className="field-row-label">
                  SFDC Lead ID
                </div>
                <div className="field-row-value">
                  {contactData.fieldValues && pathOr('N/A', ['value'], contactData.fieldValues.find(field => field.id === "100024"))}
                </div>
              </div>
              <div className="field-row">
                <div className="field-row-label">
                  First Name
                </div>
                <div className="field-row-value">
                  {pathOr('N/A', ['firstName'], contactData)}
                </div>
              </div>
              <div className="field-row">
                <div className="field-row-label">
                  Last Name
                </div>
                <div className="field-row-value">
                  {pathOr('N/A', ['lastName'], contactData)}
                </div>
              </div>
              <div className="field-row">
                <div className="field-row-label">
                  Company
                </div>
                <div className="field-row-value">
                  {pathOr('N/A', ['accountName'], contactData)}
                </div>
              </div>
              <div className="field-row">
                <div className="field-row-label">
                  Country
                </div>
                <div className="field-row-value">
                  {pathOr('N/A', ['country'], contactData)}
                </div>
              </div>
              <div className="field-row">
                <div className="field-row-label">
                  State
                </div>
                <div className="field-row-value">
                  {pathOr('N/A', ['province'], contactData)}
                </div>
              </div>
              <div className="field-row">
                <div className="field-row-label">
                  Business Phone
                </div>
                <div className="field-row-value">
                  {pathOr('N/A', ['businessPhone'], contactData)}
                </div>
              </div>
            </div>
        }
        {(hasNoData || isNil(email) || isEmpty(contactData)) &&
            <div className="contact-sidebar-enrichment-error">
              <EnrichmentError />
              <h4>We couldn&apos;t find a match for this contact in your Eloqua records</h4>
            </div>
        }
        {showSurfButton && <div className="field-row">
          <Button
            className="contact-sidebar-surf-button"
            size="small"
            type="tertiary"
            href={this.generateSurfLink()}
            target="_blank"
            disabled={hasNoData}
            onClick={() => this.props.track('Conversation Sidebar - Viewed In SURF')}>
            Search/Create Lead in SURF
          </Button>
        </div>}
      </Card>
    )
  }
}

export default withTracking(EloquaCard)
