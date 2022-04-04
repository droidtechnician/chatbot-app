import './login-page.component.css'
import { Formik } from 'formik';
import { Form, Button } from 'react-bootstrap';

export default function LoginPage() {

    return (
        <div className="form-container container">
            <div className='row'>
                <img className='chatbot-ic' />
            </div>
            <Formik
                initialValues={{ email: '', password: '' }}
                validate={values => {
                    const errors = {};
                    if (!values.email) {
                        errors.email = 'Required';
                    } else if (
                        !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)
                    ) {
                        errors.email = 'Invalid email address';
                    }
                    return errors;
                }}
                onSubmit={(values, { setSubmitting }) => {
                    setTimeout(() => {
                        alert(JSON.stringify(values, null, 2));
                        setSubmitting(false);
                    }, 400);
                }}
            >
                {({
                    values,
                    errors,
                    touched,
                    handleChange,
                    handleBlur,
                    handleSubmit,
                    isSubmitting,
                    /* and other goodies */
                }) => (
                    <Form onSubmit={handleSubmit} className="row col-md-6 col-xl-4">
                        <Form.Group className="mb-3" controlId="loginForm.emailId">
                            <Form.Control type="email" name="email" placeholder="name@example.com"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.email} />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="loginForm.password">
                            <Form.Control type="password" name="password"
                                onChange={handleChange}
                                onBlur={handleBlur}
                                value={values.password} />
                        </Form.Group>
                        <Form.Group>
                            <Button variant="primary" type="submit" disabled={isSubmitting} className="col-12">Login</Button>
                        </Form.Group>
                    </Form>
                )}
            </Formik>
        </div>
    )
}
